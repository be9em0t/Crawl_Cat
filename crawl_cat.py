#!/usr/bin/env python3
"""
Crawl4ai CLI Wrapper

A wrapper script for the crwl CLI command that reads configuration from a single YAML file
instead of requiring multiple separate YAML files.

Usage:
    python crawl_cat.py -cfg config_shadergraph.yaml
"""

import argparse
import os
import subprocess
import sys
import tempfile
import yaml
from pathlib import Path
from typing import Dict, Any, Optional


def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    if not os.path.exists(config_path):
        print(f"Error: Configuration file '{config_path}' not found.")
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_file_extension(output_format: str) -> str:
    """Get file extension based on output format."""
    format_extensions = {
        'markdown': '.md',
        'md': '.md',
        'json': '.json',
        'html': '.html',
        'txt': '.txt'
    }
    return format_extensions.get(output_format.lower(), '.txt')


def display_config_summary(config: Dict[str, Any], global_config: Dict[str, Any] = None):
    """Display a summary of the parsed configuration."""
    print("🔧 Configuration Summary:")
    print(f"   URL: {config.get('url', 'N/A')}")
    print(f"   Output Format: {config.get('output_format', 'N/A')}")

    if 'save' in config and 'output_format' in config:
        extension = get_file_extension(config['output_format'])
        save_folder = config.get('save_folder')
        if not save_folder and global_config:
            save_folder = global_config.get('save_folder')

        if save_folder:
            output_path = os.path.join(save_folder, f"{config['save']}{extension}")
        else:
            output_path = f"{config['save']}{extension}"
        print(f"   Save Path: {output_path}")

    if 'browser' in config:
        browser = config['browser']
        print(f"   Browser: viewport={browser.get('viewport_width', 'N/A')}, headless={browser.get('headless', 'N/A')}")

    if 'crawler' in config:
        crawler = config['crawler']
        css_selector = crawler.get('css_selector', 'None (full page)')
        print(f"   Crawler: css_selector={css_selector}, cache_mode={crawler.get('cache_mode', 'N/A')}")

    print("🚀 Starting crawler...\n")


def create_temp_yaml(data: Dict[str, Any], suffix: str) -> str:
    """Create a temporary YAML file with the given data."""
    with tempfile.NamedTemporaryFile(mode='w', suffix=f'_{suffix}.yml', delete=False) as f:
        yaml.dump(data, f, default_flow_style=False)
        return f.name


def build_crwl_command(config: Dict[str, Any], global_config: Dict[str, Any] = None) -> list:
    """Build the crwl command from configuration."""
    cmd = ['crwl']

    # URL is required
    if 'url' not in config:
        print("Error: 'url' is required in configuration.")
        sys.exit(1)

    cmd.append(config['url'])

    # Handle multiple URLs
    if 'urls' in config and isinstance(config['urls'], list):
        for url in config['urls'][1:]:  # First URL already added
            cmd.extend(['-u', url])

    temp_files = []

    # Browser configuration
    if 'browser' in config:
        browser_file = create_temp_yaml(config['browser'], 'browser')
        temp_files.append(browser_file)
        cmd.extend(['-B', browser_file])

    # Crawler configuration
    if 'crawler' in config:
        crawler_file = create_temp_yaml(config['crawler'], 'crawler')
        temp_files.append(crawler_file)
        cmd.extend(['-C', crawler_file])

    # Extraction configuration
    if 'extraction' in config:
        extract_file = create_temp_yaml(config['extraction'], 'extract')
        temp_files.append(extract_file)
        cmd.extend(['-e', extract_file])

        # Schema file for extraction
        if 'schema' in config:
            schema_file = create_temp_yaml(config['schema'], 'schema')
            temp_files.append(schema_file)
            cmd.extend(['-s', schema_file])

    # Filter configuration
    if 'filter' in config:
        filter_file = create_temp_yaml(config['filter'], 'filter')
        temp_files.append(filter_file)
        cmd.extend(['-f', filter_file])

    # Output format
    if 'output_format' in config:
        cmd.extend(['-o', config['output_format']])

    # Handle save field for automatic file naming
    if 'save' in config and 'output_format' in config:
        extension = get_file_extension(config['output_format'])

        # Determine save folder (per-source overrides global)
        save_folder = config.get('save_folder')
        if not save_folder and global_config:
            save_folder = global_config.get('save_folder')

        # Create folder if specified
        if save_folder:
            os.makedirs(save_folder, exist_ok=True)
            output_filename = os.path.join(save_folder, f"{config['save']}{extension}")
        else:
            output_filename = f"{config['save']}{extension}"

        cmd.extend(['-O', output_filename])
        print(f"Output will be saved to: {output_filename}")

    # Output file (manual override)
    elif 'output_file' in config:
        cmd.extend(['-O', config['output_file']])

    # Verbose
    if config.get('verbose', False):
        cmd.append('-v')

    # Cache bypass
    if config.get('bypass_cache', False):
        cmd.append('--bypass-cache')

    # Store temp files for cleanup
    cmd.append('--temp-files')
    cmd.extend(temp_files)

    return cmd


def cleanup_temp_files(temp_files: list):
    """Clean up temporary files."""
    for temp_file in temp_files:
        try:
            os.unlink(temp_file)
        except OSError:
            pass


def main():
    parser = argparse.ArgumentParser(description='Crawl4ai CLI Wrapper')
    parser.add_argument('-cfg', '--config', required=True,
                       help='Path to configuration YAML file')
    parser.add_argument('-id', '--source-id',
                       help='Specific source ID to run (if config has multiple sources)')

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Handle multiple sources
    global_config = {}
    if 'sources' in config and isinstance(config['sources'], list):
        if not args.source_id:
            print("Error: Config has multiple sources. Use -id to specify which source to run.")
            print("Available sources:", [s.get('id') for s in config['sources']])
            sys.exit(1)

        # Extract global config (everything except 'sources')
        global_config = {k: v for k, v in config.items() if k != 'sources'}

        # Find the specific source
        source_config = None
        for source in config['sources']:
            if source.get('id') == args.source_id:
                source_config = source
                break

        if not source_config:
            print(f"Error: Source '{args.source_id}' not found in config.")
            sys.exit(1)

        config = source_config

    # Build command
    cmd = build_crwl_command(config, global_config)

    # Display configuration summary
    display_config_summary(config, global_config)

    # Extract temp files for cleanup
    temp_files = []
    if '--temp-files' in cmd:
        idx = cmd.index('--temp-files')
        temp_files = cmd[idx + 1:]
        cmd = cmd[:idx]  # Remove temp files from command

    print(f"Running command: {' '.join(cmd)}")

    try:
        # Check if output is being saved to file
        saving_to_file = '--output' in cmd

        # Run the command
        result = subprocess.run(cmd, check=True, text=True, capture_output=not saving_to_file)

        if saving_to_file:
            # When saving to file, only show stderr if there are errors
            if result.stderr:
                print("STDERR:")
                print(result.stderr)
            else:
                print("Content saved to file successfully.")
        else:
            # When not saving to file, show all output
            print("STDOUT:")
            print(result.stdout)
            if result.stderr:
                print("STDERR:")
                print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        sys.exit(e.returncode)
    finally:
        # Clean up temporary files
        cleanup_temp_files(temp_files)


if __name__ == '__main__':
    main()