
--- Page 1: https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html ---

# Node library
Explore nodes that enable color and channel manipulation, mathematical and procedural generation, input data handling, custom texture management, UV mapping, utility logic, and shader data representation.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html#graph-nodes)Graph nodes
**Topic** | **Description**  
---|---  
[Artistic](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Artistic-Nodes.html) | Learn about color adjustment, blending, filtering, masking, normal map manipulation, and color space conversion.  
[Channel](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Channel-Nodes.html) | Learn about combining, splitting, reordering, or flipping vector and color channels.  
[Custom Render Texture nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Custom-Render-Texture-Nodes.html) | Learn about properties and data of custom render textures.  
[Input](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Input-Nodes.html) | Learn about values, mesh attributes, gradients, matrices, deformation data, PBR parameters, scene information, and texture sampling options.  
[Math](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Math-Nodes.html) | Learn about mathematical operations.  
[Procedural](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Procedural-Nodes.html) | Learn about creating patterns, noise textures, and geometric shapes.  
[UI](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/ui-nodes.html) | Learn about nodes specifically designed for UI elements, including render type handling, element texture sampling, and layout-based UVs.  
[Utility](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Utility-Nodes.html) | Learn about basic preview, sub-graph referencing, and essential logic operations.  
[UV](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/UV-Nodes.html) | Learn about manipulation and mapping effects, enabling advanced texture animations, coordinate transformations, and warping techniques.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html#block-nodes)Block nodes
**Topic** | **Description**  
---|---  
[Block](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Block-Node.html) | You can find these nodes in the **Vertex** and **Fragment** contexts of the Master Stack.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html#additional-resources)Additional resources
  * [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node.html)
  * [Create Node Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Create-Node-Menu.html)
  * [Shader Graph Node Reference Samples](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/ShaderGraph-Samples.html)




--- Page 2: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html ---

# Artistic nodes
Adjust colors, blend layers, filter images, mask regions, manipulate normal maps, and convert color spaces.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html#adjustment)Adjustment
**Topic** | **Description**  
---|---  
[Channel Mixer](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html) | Controls the amount each of the channels of input In contribute to each of the output channels.  
[Contrast](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Contrast-Node.html) | Adjusts the contrast of input In by the amount of input Contrast.  
[Hue](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html) | Offsets the hue of input In by the amount of input Offset.  
[Invert Colors](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html) | Inverts the colors of input In on a per channel basis.  
[Replace Color](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Replace-Color-Node.html) | Replaces values in input In equal to input From to the value of input To.  
[Saturation](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturation-Node.html) | Adjusts the saturation of input In by the amount of input Saturation.  
[White Balance](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/White-Balance-Node.html) | Adjusts the temperature and tint of input In by the amount of inputs Temperature and Tint respectively.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html#blend)Blend
**Topic** | **Description**  
---|---  
[Blend](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blend-Node.html) | Blends the value of input Blend onto input Base using the blending mode defined by parameter Mode.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html#filter)Filter
**Topic** | **Description**  
---|---  
[Dither](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dither-Node.html) | Dither is an intentional form of noise used to randomize quantization error. It is used to prevent large-scale patterns such as color banding in images..  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html#mask)Mask
**Topic** | **Description**  
---|---  
[Channel Mask](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mask-Node.html) | Masks values of input In on channels selected in dropdown Channels.  
[Color Mask](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Mask-Node.html) | Creates a mask from values in input In equal to input Mask Color.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html#normal)Normal
**Topic** | **Description**  
---|---  
[Normal Blend](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Blend-Node.html) | Blends two normal maps defined by inputs A and B together.  
[Normal From Height](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-From-Height-Node.html) | Creates a normal map from a height map defined by input Texture.  
[Normal Strength](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Strength-Node.html) | Adjusts the strength of the normal map defined by input In by the amount of input Strength.  
[Normal Unpack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Unpack-Node.html) | Unpacks a normal map defined by input In.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html#utility)Utility
**Topic** | **Description**  
---|---  
[Colorspace Conversion](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html) | Returns the result of converting the value of input In from one colorspace space to another.


--- Page 3: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Render-Texture-Nodes.html ---

# Custom Render Texture nodes
Access properties and data of custom render textures, including size, slice index, cubemap face, and previous update state.
**Topic** | **Description**  
---|---  
[Custom Render Texture Slice](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Slice.html) | Access the custom render texture slice index and cubemap face.  
[Custom Render Texture Size](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Size.html) | Access the custom render texture size.  
[Custom Render Texture Self](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Self.html) | Access the custom render texture from the previous update.


--- Page 4: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html ---

# Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html#description)Description
A **Node** defines an input, output or operation on the Shader Graph, depending on its available [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html). A **Node** may have any number of input and/or output ports. You create a Shader Graph by connecting these ports with [Edges](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html). A **Node** might also have any number of **Controls** , these are controls on the **Node** that do not have ports.
You can collapse a **Node** by clicking the **Collapse** button in the top-right corner of the **Node**. This will hide all unconnected ports.
For components of a **Node** see:
  * [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html)
  * [Edge](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html)


There are many available **Nodes** in Shader Graph. For a full list of all available **Nodes** see the [Node Library](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node-Library.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html#preview)Preview
Many nodes include a preview. This preview displays the main output value at that stage in the graph. Hide this preview with the Collapse control that displays when you hover over the node. You can also collapse and expand node previews via the Context Menu in the [Shader Graph Window](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html). To configure the appearance of node previews, see [Preview Mode Control](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Mode-Control.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html#context-menu)Context Menu
Right clicking on a **Node** will open a context menu. This menu contains many operations that can be performed on the **Node**. Note that when multiple nodes are selected, these operations will be applied to the entire selection.
Item | Description  
---|---  
Copy Shader | Copies the generated HLSL code at this stage in the graph to the clipboard  
Disconnect All | Removes all edges from all ports on the **Node(s)**  
Cut | Cuts selected **Node(s)** to the clipboard  
Copy | Copies selected **Nodes(s)** to the clipboard  
Paste | Pastes **Node(s)** in the clipboard  
Delete | Deletes selected **Node(s)**  
Duplicate | Duplicates selected **Node(s)**  
Convert To Sub-graph | Creates a new [Sub-graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html) with the selected **Node(s)** included  
Convert To Inline Node | Converts a [Property Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html) into a regular node of the appropriate [Data Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html)  
Convert To Property | Converts a **Node** into a new **Property** on the [Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackboard.html) of the appropriate [Property Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html)  
Open Documentation | Opens a new web browser to the selected **Nodes** documentation page in the [Node Library](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node-Library.html)  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html#color-mode)Color Mode
**Nodes** interact with the Shader Graph Window's Color Modes. Colors are displayed on nodes underneath the text on the node title bar. See [Color Modes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Modes.html) for more information on available colors for nodes.


--- Page 5: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Procedural-Nodes.html ---

# Procedural nodes
Generate patterns, noise textures, and customizable geometric shapes procedurally using UV input.
**Topic** | **Description**  
---|---  
[Checkerboard](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Checkerboard-Node.html) | Generates a checkerboard of alternating colors between inputs Color A and Color B based on input UV.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Procedural-Nodes.html#noise)Noise
**Topic** | **Description**  
---|---  
[Gradient Noise](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html) | Generates a gradient, or Perlin, noise based on input UV.  
[Simple Noise](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Simple-Noise-Node.html) | Generates a simple, or Value, noise based on input UV.  
[Voronoi](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html) | Generates a Voronoi, or Worley, noise based on input UV.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Procedural-Nodes.html#shape)Shape
**Topic** | **Description**  
---|---  
[Ellipse](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ellipse-Node.html) | Generates an ellipse shape based on input UV at the size specified by inputs Width and Height.  
[Polygon](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polygon-Node.html) | Generates a regular polygon shape based on input UV at the size specified by inputs Width and Height. The polygon's amount of sides is determined by input Sides.  
[Rectangle](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rectangle-Node.html) | Generates a rectangle shape based on input UV at the size specified by inputs Width and Height.  
[Rounded Polygon](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Polygon-Node.html) | Generates a rounded polygon shape based on input UV at the size specified by inputs Width and Height. The input Sides specifies the number of sides, and the input Roundness defines the roundness of each corner.  
[Rounded Rectangle](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Rectangle-Node.html) | Generates a rounded rectangle shape based on input UV at the size specified by inputs Width and Height. The input Radius defines the radius of each corner.


--- Page 6: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html ---

# Create Node Menu
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html#description)Description
Use the **Create Node Menu** to create [nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) in Shader Graph. To open the **Create Node Menu** , either right-click on the workspace in the [Shader Graph Window](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html) and select **Create Node** , or press the spacebar.
At the top of the **Create Node Menu** is a search bar. To search for a node, type any part of its name in the search field. The search box gives you autocomplete options, and you can press Tab to accept the predictive text. It highlights matching text in yellow.
The **Create Node Menu** lists all nodes that are available in Shader Graph, categorized by their function. User-created [Sub Graphs](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html) are also available in the **Create Node Menu** under **Sub Graph Assets** , or in a custom category that you define in the Sub Graph Asset.
To add a node to the workspace, double-click it in the **Create Node Menu**.
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html#contextual-create-node-menu)Contextual Create Node Menu
A contextual **Create Node Menu** filters the available nodes, and only shows those that use the [Data Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) of a selected edge. It lists every available [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) on nodes that match that Data Type.
To open a contextual **Create Node Menu** , click and drag an [Edge](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) from a Port, and then release it in an empty area of the workspace.
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html#master-stack-create-node-menu)Master Stack Create Node Menu
To add a new [Block Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html) to the [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html), either right click and select **Create Node** or press spacebar with the stack selected.
The **Create Node Menu** will display all available blocks for the master stack based on the render pipelines in your project. Any block can be added to the master stack via the **Create Node Menu**. If the block added is not compatible with the current Graph settings, the block will be disabled until the settings are configured to support it.


--- Page 7: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Nodes.html ---

# UV nodes
Create texture animations, coordinate transformations, and warping through UV manipulation and mapping effects.
**Topic** | **Description**  
---|---  
[Flipbook](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html) | Creates a flipbook, or texture sheet animation, of the UVs supplied to input In.  
[Radial Shear](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radial-Shear-Node.html) | Applies a radial shear warping effect similar to a wave to the value of input UV.  
[Spherize](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Spherize-Node.html) | Applies a spherical warping effect similar to a fisheye camera lens to the value of input UV.  
[Triplanar](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html) | A method of generating UVs and sampling a texture by projecting in world space.  
[Parallax Mapping](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Mapping-Node.html) | Creates a parallax effect that displaces a material's UVs.  
[Polar Coordinates](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polar-Coordinates-Node.html) | Converts the value of input UV to polar coordinates.  
[Rotate](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-Node.html) | Rotates the value of input UV around a reference point defined by input Center by the amount of input Rotation.  
[Tiling and Offset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html) | Tiles and offsets the value of input UV by the inputs Tiling and Offset respectively.  
[Twirl](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Twirl-Node.html) | Applies a twirl warping effect similar to a black hole to the value of input UV.  
[Parallax Occlusion Mapping](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Occlusion-Mapping-Node.html) | Creates a parallax effect that displaces a material's UVs and depth.


--- Page 8: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Utility-Nodes.html ---

# Utility nodes
Enable essential logic operations, previews, and sub-graph referencing.
**Topic** | **Description**  
---|---  
[Preview](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html) | Provides a preview window and passes the input value through without modification.  
[Sub-Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html) | Provides a reference to a Sub-graph asset.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Utility-Nodes.html#logic)Logic
**Topic** | **Description**  
---|---  
[All](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/All-Node.html) | Returns true if all components of the input In are non-zero.  
[And](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/And-Node.html) | Returns true if both the inputs A and B are true.  
[Any](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Any-Node.html) | Returns true if any of the components of the input In are non-zero.  
[Branch](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html) | Provides a dynamic branch to the shader.  
[Comparison](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Comparison-Node.html) | Compares the two input values A and B based on the condition selected on the dropdown.  
[Is Infinite](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-Infinite-Node.html) | Returns true if any of the components of the input In is an infinite value.  
[Is NaN](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-NaN-Node.html) | Returns true if any of the components of the input In is not a number (NaN).  
[Nand](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Nand-Node.html) | Returns true if both the inputs A and B are false.  
[Not](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Not-Node.html) | Returns the opposite of input In. If In is true, the output is false. Otherwise, it returns true.  
[Or](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Or-Node.html) | Returns true if either input A or input B is true.


--- Page 9: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html ---

# Math nodes
Perform a mathematical operations, from basic arithmetic to advanced functions like trigonometry, vectors, matrices, interpolation, and waves.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#advanced)Advanced
**Topic** | **Description**  
---|---  
[Absolute](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Absolute-Node.html) | Returns the absolute value of input In.  
[Exponential](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html) | Returns the exponential value of input In.  
[Length](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Length-Node.html) | Returns the length of input In.  
[Log](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html) | Returns the logarithm of input In.  
[Modulo](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Modulo-Node.html) | Returns the remainder of input A divided by input B.  
[Negate](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Negate-Node.html) | Returns the inverse value of input In.  
[Normalize](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normalize-Node.html) | Returns the normalized vector of input In.  
[Posterize](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Posterize-Node.html) | Returns the input In converted into a number of values defined by input Steps.  
[Reciprocal](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Node.html) | Returns the result of 1 divided by input In.  
[Reciprocal Square Root](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Square-Root-Node.html) | Returns the result of 1 divided by the square root of input In.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#basic)Basic
**Topic** | **Description**  
---|---  
[Add](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Add-Node.html) | Returns the sum of the two input values.  
[Divide](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Divide-Node.html) | Returns the result of input A divided by input B.  
[Multiply](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Multiply-Node.html) | Returns the result of input A multiplied by input B.  
[Power](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Power-Node.html) | Returns the result of input A to the power of input B.  
[Square Root](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Square-Root-Node.html) | Returns the square root of input In.  
[Subtract](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Subtract-Node.html) | Returns the result of input A minus input B.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#derivative)Derivative
**Topic** | **Description**  
---|---  
[DDX](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDX-Node.html) | Returns the partial derivative with respect to the screen-space x-coordinate.  
[DDXY](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDXY-Node.html) | Returns the sum of both partial derivatives.  
[DDY](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDY-Node.html) | Returns the partial derivative with respect to the screen-space y-coordinate.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#interpolation)Interpolation
**Topic** | **Description**  
---|---  
[Inverse Lerp](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Inverse-Lerp-Node.html) | Returns the parameter that produces the interpolant specified by input T within the range of input A to input B.  
[Lerp](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html) | Returns the result of linearly interpolating between input A and input B by input T.  
[Smoothstep](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Smoothstep-Node.html) | Returns the result of a smooth Hermite interpolation between 0 and 1, if input In is between inputs Edge1 and Edge2.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#matrix)Matrix
**Topic** | **Description**  
---|---  
[Matrix Construction](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Construction-Node.html) | Constructs square matrices from the four input vectors M0, M1, M2 and M3.  
[Matrix Determinant](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Determinant-Node.html) | Returns the determinant of the matrix defined by input In.  
[Matrix Split](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html) | Splits a square matrix defined by input In into vectors.  
[Matrix Transpose](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Transpose-Node.html) | Returns the transposed value of the matrix defined by input In.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#range)Range
**Topic** | **Description**  
---|---  
[Clamp](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Clamp-Node.html) | Returns the input In clamped between the minimum and maximum values defined by inputs Min and Max respectively.  
[Fraction](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html) | Returns the fractional (or decimal) part of input In; which is greater than or equal to 0 and less than 1.  
[Maximum](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Maximum-Node.html) | Returns the largest of the two inputs values A and B.  
[Minimum](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Minimum-Node.html) | Returns the smallest of the two inputs values A and B.  
[One Minus](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/One-Minus-Node.html) | Returns the result of input In subtracted from 1.  
[Random Range](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Random-Range-Node.html) | Returns a pseudo-random number that is between the minimum and maximum values defined by inputs Min and Max.  
[Remap](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Remap-Node.html) | Remaps the value of input In from between the values of input Out Min Max to between the values of input In Min Max.  
[Saturate](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturate-Node.html) | Returns the value of input In clamped between 0 and 1.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#round)Round
**Topic** | **Description**  
---|---  
[Ceiling](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ceiling-Node.html) | Returns the smallest integer value, or whole number, that is greater than or equal to the value of input In.  
[Floor](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Floor-Node.html) | Returns the largest integer value, or whole number, that is less than or equal to the value of input In.  
[Round](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Round-Node.html) | Returns the value of input In rounded to the nearest integer, or whole number.  
[Sign](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sign-Node.html) | Returns -1 if the value of input In is less than zero, 0 if equal to zero and 1 if greater than zero.  
[Step](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Step-Node.html) | Returns 1 if the value of input In is greater than or equal to the value of input Edge, otherwise returns 0.  
[Truncate](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Truncate-Node.html) | Returns the integer, or whole number, component of the value of input In.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#trigonometry)Trigonometry
**Topic** | **Description**  
---|---  
[Arccosine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Arccosine-Node.html) | Returns the arccosine of each component the input In as a vector of equal length.  
[Arcsine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Arcsine-Node.html) | Returns the arcsine of each component the input In as a vector of equal length.  
[Arctangent](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Arctangent-Node.html) | Returns the arctangent of the value of input In. Each component should be within the range of -Pi/2 to Pi/2.  
[Arctangent2](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Arctangent2-Node.html) | Returns the arctangent of the values of both input A and input B.  
[Cosine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Cosine-Node.html) | Returns the cosine of the value of input In.  
[Degrees to Radians](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Degrees-To-Radians-Node.html) | Returns the value of input In converted from degrees to radians.  
[Hyperbolic Cosine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hyperbolic-Cosine-Node.html) | Returns the hyperbolic cosine of input In.  
[Hyperbolic Sine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hyperbolic-Sine-Node.html) | Returns the hyperbolic sine of input In.  
[Hyperbolic Tangent](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hyperbolic-Tangent-Node.html) | Returns the hyperbolic tangent of input In.  
[Radians to Degrees](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radians-To-Degrees-Node.html) | Returns the value of input In converted from radians to degrees.  
[Sine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sine-Node.html) | Returns the sine of the value of input In.  
[Tangent](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tangent-Node.html) | Returns the tangent of the value of input In.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#vector)Vector
**Topic** | **Description**  
---|---  
[Cross Product](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Cross-Product-Node.html) | Returns the cross product of the values of the inputs A and B.  
[Distance](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Distance-Node.html) | Returns the Euclidean distance between the values of the inputs A and B.  
[Dot Product](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dot-Product-Node.html) | Returns the dot product, or scalar product, of the values of the inputs A and B.  
[Fresnel Effect](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fresnel-Effect-Node.html) | Fresnel Effect is the effect of differing reflectance on a surface depending on viewing angle, where as you approach the grazing angle more light is reflected.  
[Projection](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Projection-Node.html) | Returns the result of projecting the value of input A onto a straight line parallel to the value of input B.  
[Reflection](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Node.html) | Returns a reflection vector using input In and a surface normal Normal.  
[Rejection](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rejection-Node.html) | Returns the result of the projection of the value of input A onto the plane orthogonal, or perpendicular, to the value of input B.  
[Rotate About Axis](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-About-Axis-Node.html) | Rotates the input vector In around the axis Axis by the value of Rotation.  
[Sphere Mask](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sphere-Mask-Node.html) | Creates a sphere mask originating from input Center.  
[Transform](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transform-Node.html) | Returns the result of transforming the value of input In from one coordinate space to another.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html#wave)Wave
**Topic** | **Description**  
---|---  
[Noise Sine Wave](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Noise-Sine-Wave-Node.html) | Returns the sine of the value of input In. For variance, random noise is added to the amplitude of the sine wave.  
[Sawtooth Wave](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sawtooth-Wave-Node.html) | Returns a sawtooth wave from the value of input In.  
[Matrix Split](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html) | Splits a square matrix defined by input In into vectors.  
[Matrix Transpose](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Transpose-Node.html) | Returns the transposed value of the matrix defined by input In.


--- Page 10: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ui-nodes.html ---

# UI nodes
**Topic** | **Description**  
---|---  
[Default Solid](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html) | Outputs the solid color specified for your UI elements.  
[Default Texture](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html) | Provides a pre-defined texture for your UI elements.  
[Default SDF Text](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html) | Provides the text color set for SDF text rendering and includes a tint input to modify the color of the text.  
[Default Bitmap Text](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-bitmap-text-node.html) | Provides the text color set for bitmap text rendering and includes a tint input to modify the color of the text.  
[Default Gradient](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html) | Outputs the gradient specified for your UI elements.  
[Render Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/render-type-node.html) | Outputs the current render type for conditional logic in the shader.  
[Render Type Branch](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/render-type-branch-node.html) | Routes inputs based on the current render type and outputs the appropriate result.  
[Sample Element Texture](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/sample-element-texture-node.html) | Samples a texture at specific UV coordinates.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ui-nodes.html#additional-resources)Additional resources
  * [Create and apply custom shaders](xref:uie-create-apply-custom-shaders)




--- Page 11: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ShaderGraph-Samples.html ---

# Shader Graph samples
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ShaderGraph-Samples.html#description)Description
The Shader Graph package offers sample Assets, which you can download through **Package Manager**. When you import these samples, Unity places the files in your Project's Asset folder. The files contain examples that demonstrate how to use Shader Graph features.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ShaderGraph-Samples.html#add-samples)Add samples
To add samples to your project:
  1. In the main menu, go to **Window** > **Package Management** > **Package Manager**.
  2. Select **Shader Graph** from the list of packages.
  3. In the **Samples** section, select **Import** next to a sample.
  4. Open the sample assets from the `Assets/Samples/Shader Graph/<your version>/` folder.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ShaderGraph-Samples.html#available-samples)Available samples
The following samples are currently available for Shader Graph.
Procedural Patterns  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Patterns_Page.png)  
This collection of Assets showcases various procedural techniques possible with Shader Graph. Use them directly in your Project, or edit them to create other procedural patterns. The patterns in this collection are: Bacteria, Brick, Dots, Grid, Herringbone, Hex Lattice, Houndstooth, Smooth Wave, Spiral, Stripes, Truchet, Whirl, Zig Zag.  
Node Reference  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/NodeReferenceSamples.png)  
This set of Shader Graph assets provides reference material for the nodes available in the Shader Graph node library. Each graph contains a description for a specific node, examples of how it can be used, and useful tips. Some example assets also show a break-down of the math that the node is doing. You can use these samples along with the documentation to learn more about the behavior of individual nodes.  
[Feature Examples](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html)  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/FeatureExamplesSample.png)  
This is a collection of over 30 Shader Graph files. Each file demonstrates a specific shader technique such as angle blending, triplanar projection, parallax mapping, and custom lighting. While you won’t use these shaders directly in your project, you can use them to quickly learn and understand the various techniques, and recreate them into your own work. Each file contains notes that describe what the shader is doing, and most of the shaders are set up with the core functionality contained in a subgraph that’s easy to copy and paste directly into your own shader. The sample also has extensive documentation describing each of the samples to help you learn.  
[Production Ready Shaders](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready.html)  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/ProductionReadySample.png)  
The Shader Graph Production Ready Shaders sample is a collection of Shader Graph shader assets that are ready to be used out of the box or modified to suit your needs. You can take them apart and learn from them, or just drop them directly into your project and use them as they are. The sample includes the Shader Graph versions of the HDRP and URP Lit shaders. It also includes a step-by-step tutorial for how to combine several of the shaders to create a forest stream environment.  
[UGUI Shaders](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders.html)  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/UIToolsSample.png)  
The Shader Graph UGUI Shaders sample is a collection of Shader Graph subgraphs that you can use to build user interface elements. They speed up the process of building widgets, buttons, and backgrounds for the user interface of your project. With these tools, you can build dynamic, procedural UI elements that don’t require any texture memory and scale correctly for any resolution screen. In addition to the subgraphs, the sample also includes example buttons, indicators, and backgrounds built with the subgraphs. The examples show how the subgraphs function in context and help you learn how to use them.  
Custom Material Property Drawers  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/CustomMaterialPropertySample.png)  
This sample contains an example of a Custom Material Property Drawer that allows using a Min/Max Slider to control a Vector2 x and y values, often used for range remapping. It comes with a documented Shader Graph example.  
[Custom Lighting](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting.html)  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/CustomLightingSample.png)  
The Shader Graph Custom Lighting sample shows how you can create your own custom lighting model in Shader Graph and provides dozens of example templates, shaders, and subgraphs to help you get started with your own custom lighting.  
[Terrain Shaders](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Terrain-Shaders.html)  
---  
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/TerrainSample.png)  
The Shader Graph Terrain Sample provides example shaders to learn from and subgraphs that you can use to build your own terrain shaders. Custom terrain shaders can use more advanced features like hexagon tile break-up, parallax occlusion mapping, or triplanar projection. Or you can use techniques like array texture sampling or alternate texture packing methods to make the shader cheaper to render than the default one. Whether you're making faster or more advanced terrain shaders, this sample will help you get the results you're looking for.


--- Page 12: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Nodes.html ---

# Channel nodes
Combine, split, reorder, or flip vector and color channels.
**Topic** | **Description**  
---|---  
[Append](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html) | Combine two float or vector inputs into a single new vector of variable dimensions.  
[Combine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html) | Creates new vectors from the four inputs R, G, B and A.  
[Flip](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html) | Flips the individual channels of input In selected by the node's parameters.  
[Split](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html) | Splits the input vector In into four Float outputs R, G, B and A.  
[Swizzle](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html) | Creates a new vector from the reordered elements of the input vector.


--- Page 13: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html ---

# Block Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html#description)Description
A Block is a specific type of node for the Master Stack. A Block represents a single piece of the surface (or vertex) description data that Shader Graph uses in the final shader output. [Built In Block nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Built-In-Blocks.html) are always available, but nodes that are specific to a certain render pipeline are only available for that pipeline. For example, Universal Block nodes are only available for the Universal Render Pipeline (URP), and High Definition Block nodes are only available for the High Definition Render Pipeline (HDRP).
Some blocks are only compatible with specific [Graph Settings](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html), and might become active or inactive based on the graph settings you select. You can't cut, copy, or paste Blocks.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html#add-and-remove-block-nodes)Add and Remove Block Nodes
To add a new Block node to a Context in the Master Stack, place the cursor over an empty area in the Context, then press the Spacebar or right-click and select **Create Node**.
This brings up the Create Node menu, which displays only Block nodes that are valid for the Context. For example, Vertex Blocks don't appear in the Create Node menu of a Fragment Context.
Select a Block node from the menu to add it to the Context. To remove a Block from the Context, select the Block node in the Context, then press the Delete key or right-click and select **Delete**.
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html#automatically-add-or-remove-blocks)Automatically Add or Remove Blocks
You can also enable or disable an option in the Shader Graph Preferences to automatically add and remove Blocks from a Context.
If you enable **Automatically Add or Remove Blocks** , Shader Graph automatically adds the required Block nodes for that particular asset's Target or material type. It automatically removes any incompatible Block nodes that have no connections and default values.
If you disable **Automatically Add or Remove Blocks** , Shader Graph doesn't automatically add and remove Block nodes. You must manually add and remove all Block nodes.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html#active-and-inactive-blocks)Active and Inactive Blocks
Active Block nodes are Blocks that contribute to the final shader. Inactive Block nodes are Blocks that are present in the Shader Graph, but don't contribute to the final shader.
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Active-Inactive-Blocks.PNG)
When you change the graph settings, certain Blocks might become active or inactive. Inactive Block nodes and any node streams that are connected only to Inactive Block nodes appear grayed out.


--- Page 14: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node-Library.html ---

# Node library
Explore nodes that enable color and channel manipulation, mathematical and procedural generation, input data handling, custom texture management, UV mapping, utility logic, and shader data representation.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node-Library.html#graph-nodes)Graph nodes
**Topic** | **Description**  
---|---  
[Artistic](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Artistic-Nodes.html) | Learn about color adjustment, blending, filtering, masking, normal map manipulation, and color space conversion.  
[Channel](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Nodes.html) | Learn about combining, splitting, reordering, or flipping vector and color channels.  
[Custom Render Texture nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Render-Texture-Nodes.html) | Learn about properties and data of custom render textures.  
[Input](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html) | Learn about values, mesh attributes, gradients, matrices, deformation data, PBR parameters, scene information, and texture sampling options.  
[Math](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html) | Learn about mathematical operations.  
[Procedural](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Procedural-Nodes.html) | Learn about creating patterns, noise textures, and geometric shapes.  
[UI](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ui-nodes.html) | Learn about nodes specifically designed for UI elements, including render type handling, element texture sampling, and layout-based UVs.  
[Utility](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Utility-Nodes.html) | Learn about basic preview, sub-graph referencing, and essential logic operations.  
[UV](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Nodes.html) | Learn about manipulation and mapping effects, enabling advanced texture animations, coordinate transformations, and warping techniques.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node-Library.html#block-nodes)Block nodes
**Topic** | **Description**  
---|---  
[Block](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html) | You can find these nodes in the **Vertex** and **Fragment** contexts of the Master Stack.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node-Library.html#additional-resources)Additional resources
  * [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html)
  * [Create Node Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html)
  * [Shader Graph Node Reference Samples](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/ShaderGraph-Samples.html)




--- Page 15: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html ---

# Input nodes
Supply shaders with essential data such as constants, mesh attributes, gradients, matrices, deformation, PBR parameters, scene details, and texture sampling options.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#basic)Basic
**Topic** | **Description**  
---|---  
[Boolean](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html) | Defines a constant Boolean value in the shader.  
[Color](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html) | Defines a constant Vector 4 value in the shader using a Color field.  
[Constant](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html) | Defines a Float of a mathematical constant value in the shader.  
[Integer](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html) | Defines a constant Float value in the shader using an Integer field.  
[Slider](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html) | Defines a constant Float value in the shader using a Slider field.  
[Time](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html) | Provides access to various Time parameters in the shader.  
[Float](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Float-Node.html) | Defines a Float value in the shader.  
[Vector 2](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-2-Node.html) | Defines a Vector 2 value in the shader.  
[Vector 3](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-3-Node.html) | Defines a Vector 3 value in the shader.  
[Vector 4](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-4-Node.html) | Defines a Vector 4 value in the shader.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#geometry)Geometry
**Topic** | **Description**  
---|---  
[Bitangent Vector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Bitangent-Vector-Node.html) | Provides access to the mesh vertex or fragment's Bitangent Vector.  
[Normal Vector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Vector-Node.html) | Provides access to the mesh vertex or fragment's Normal Vector.  
[Position](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Position-Node.html) | Provides access to the mesh vertex or fragment's Position.  
[Screen Position](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html) | Provides access to the mesh vertex or fragment's Screen Position.  
[Tangent Vector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tangent-Vector-Node.html) | Provides access to the mesh vertex or fragment's Tangent Vector.  
[UV](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Node.html) | Provides access to the mesh vertex or fragment's UV coordinates.  
[Vertex Color](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-Color-Node.html) | Provides access to the mesh vertex or fragment's Vertex Color value.  
[View Direction](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/View-Direction-Node.html) | Provides access to the mesh vertex or fragment's View Direction vector.  
[Vertex ID](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-ID-Node.html) | Provides access to the mesh vertex or fragment's Vertex ID value.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#gradient)Gradient
**Topic** | **Description**  
---|---  
[Blackbody](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackbody-Node.html) | Samples a radiation based gradient from temperature input (in Kelvin).  
[Gradient](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Node.html) | Defines a constant Gradient in the shader.  
[Sample Gradient](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Gradient-Node.html) | Samples a Gradient given the input of Time.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#matrix)Matrix
**Topic** | **Description**  
---|---  
[Matrix 2x2](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-2x2-Node.html) | Defines a constant Matrix 2x2 value in the shader.  
[Matrix 3x3](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-3x3-Node.html) | Defines a constant Matrix 3x3 value in the shader.  
[Matrix 4x4](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-4x4-Node.html) | Defines a constant Matrix 4x4 value in the shader.  
[Transformation Matrix](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transformation-Matrix-Node.html) | Defines a constant Matrix 4x4 value for a default Unity Transformation Matrix in the shader.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#mesh-deformation)Mesh Deformation
**Topic** | **Description**  
---|---  
[Compute Deformation Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Compute-Deformation-Node.html) | Passes compute deformed vertex data to a vertex shader. Only works with the [Entities Graphics package](https://docs.unity3d.com/Packages/com.unity.entities.graphics@latest/).  
[Linear Blend Skinning Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Linear-Blend-Skinning-Node.html) | Applies Linear Blend Vertex Skinning. Only works with the [Entities Graphics package](https://docs.unity3d.com/Packages/com.unity.entities.graphics@latest/).  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#sprite-deformation)Sprite Deformation
**Topic** | **Description**  
---|---  
[Sprite Skinning Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sprite-Skinning-Node.html) | Applies Vertex Skinning on Sprites. Only works with the [2D Animation](https://docs.unity3d.com/Packages/com.unity.2d.animation@latest/).  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#pbr)PBR
**Topic** | **Description**  
---|---  
[Dielectric Specular](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dielectric-Specular-Node.html) | Returns a Dielectric Specular F0 value for a physically based material.  
[Metal Reflectance](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Metal-Reflectance-Node.html) | Returns a Metal Reflectance value for a physically based material.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#scene)Scene
**Topic** | **Description**  
---|---  
[Ambient](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ambient-Node.html) | Provides access to the Scene's Ambient color values.  
[Camera](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Camera-Node.html) | Provides access to various parameters of the current Camera.  
[Fog](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fog-Node.html) | Provides access to the Scene's Fog parameters.  
[Baked GI](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html) | Provides access to the Baked GI values at the vertex or fragment's position.  
[Object](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Object-Node.html) | Provides access to various parameters of the Object.  
[Reflection Probe](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Probe-Node.html) | Provides access to the nearest Reflection Probe to the object.  
[Scene Color](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Color-Node.html) | Provides access to the current Camera's color buffer.  
[Scene Depth](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Depth-Node.html) | Provides access to the current Camera's depth buffer.  
[Screen](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Node.html) | Provides access to parameters of the screen.  
[Eye Index](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Eye-Index-Node.html) | Provides access to the Eye Index when stereo rendering.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#texture)Texture
**Topic** | **Description**  
---|---  
[Cubemap Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Cubemap-Asset-Node.html) | Defines a constant Cubemap Asset for use in the shader.  
[Sample Cubemap](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Cubemap-Node.html) | Samples a Cubemap and returns a Vector 4 color value for use in the shader.  
[Sample Reflected Cubemap Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Reflected-Cubemap-Node.html) | Samples a Cubemap with reflected vector and returns a Vector 4 color value for use in the shader.  
[Sample Texture 2D](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Node.html) | Samples a Texture 2D and returns a color value for use in the shader.  
[Sample Texture 2D Array](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Array-Node.html) | Samples a Texture 2D Array at an Index and returns a color value for use in the shader.  
[Sample Texture 2D LOD](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-LOD-Node.html) | Samples a Texture 2D at a specific LOD and returns a color value for use in the shader.  
[Sample Texture 3D](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-3D-Node.html) | Samples a Texture 3D and returns a color value for use in the shader.  
[Sample Virtual Texture](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Virtual-Texture-Node.html) | Samples a Virtual Texture and returns color values for use in the shader.  
[Sampler State](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sampler-State-Node.html) | Defines a Sampler State for sampling textures.  
[Texture Size](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Texture-Size-Node.html) | Returns the Width and Height of the texel size of Texture 2D input.  
[Texture 2D Array Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Texture-2D-Array-Asset-Node.html) | Defines a constant Texture 2D Array Asset for use in the shader.  
[Texture 2D Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Texture-2D-Asset-Node.html) | Defines a constant Texture 2D Asset for use in the shader.  
[Texture 3D Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Texture-3D-Asset-Node.html) | Defines a constant Texture 3D Asset for use in the shader.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html#ui)UI
**Topic** | **Description**  
---|---  
[Element Texture UV](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/element-texture-uv-node.html) | Provides the texture coordinates (UV) typically used to sample the texture assigned to a UI element.  
[Element Layout UV](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/element-layout-uv-node.html) | Provides the layout UV coordinates within a UI element's layout rectangle.  
[Element Texture Size](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/element-texture-size-node.html) | Provides the size of the texture assigned to a UI element.


--- Page 16: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Absolute-Node.html ---

# Absolute Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Absolute-Node.html#description)Description
Returns the absolute value of the input **In**. Components of the input Dynamic Vector that are positive will remain positive and components that are negative will be inverted and become positive.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Absolute-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Absolute-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Absolute_float4(float4 In, out float4 Out)
{
    Out = abs(In);
}

```



--- Page 17: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Self.html ---

# Custom Render Texture Self Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Self.html#description)Description
Provides the texture that contains the result of the previous update of the **Custom Render Texture**. Use the output that corresponds to the type of **Custom Render Texture** used.
For more information on Custom Render Textures, refer to the [Unity Manual](https://docs.unity3d.com/Manual/class-CustomRenderTexture.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Self.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Self Texture 2D | Output | Texture2D | None | 2D Texture object that contains the update result of the previous **Custom Render Texture**.  
Self Texture Cube | Output | Cubemap | None | Cubemap object that contains the update result of the previous **Custom Render Texture**.  
Self Texture 3D | Output | Texture3D | None | 3D Texture object that contains the update result of the previous **Custom Render Texture**.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Self.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
UnityBuildTexture2DStructNoScale(_SelfTexture2D)

```



--- Page 18: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html ---

# Channel Mixer Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html#description)Description
Controls the amount each of the channels of input **In** contribute to each of the channels of output **Out**. The slider parameters on the node control the contribution of each of the input channels. The toggle button parameters control which of the output channels is currently being edited. Slider controls for editing the contribution of each input channnel range between -2 and 2.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Toggle Button Array | R, G, B | Selects the output channel to edit.  
R | Slider |  | Controls contribution of input red channel to selected output channel.  
G | Slider |  | Controls contribution of input green channel to selected output channel.  
B | Slider |  | Controls contribution of input blue channel to selected output channel.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html#shader-function)Shader Function
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
_ChannelMixer_Red = float3 (OutRedInRed, OutRedInGreen, OutRedInBlue);
_ChannelMixer_Green = float3 (OutGreenInRed, OutGreenInGreen, OutGreenInBlue);
_ChannelMixer_Blue = float3 (OutBlueInRed, OutBlueInGreen, OutBlueInBlue);

void Unity_ChannelMixer_float(float3 In, float3 _ChannelMixer_Red, float3 _ChannelMixer_Green, float3 _ChannelMixer_Blue, out float3 Out)
{
    Out = float3(dot(In, _ChannelMixer_Red), dot(In, _ChannelMixer_Green), dot(In, _ChannelMixer_Blue));
}

```



--- Page 19: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html ---

# Edge
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html#description)Description
An **Edge** defines a connection between two [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html). **Edges** define how data flows through the [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html) node network. They can only be connected from an input [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) to an output [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html).
Each **Edge** has a [Data Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) which defines what [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) it can be connected to. Each [Data Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) has an associated color for identifying its type.
You can create a new **Edge** by clicking and dragging from a [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) with the left mouse button. Edges can be deleted with Delete (Windows), Command + Backspace (OSX) or from the context menu by right clicking on the [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
You can open a contextual [Create Node Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html) by dragging an **Edge** from a [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) with the left mouse button and releasing it in an empty area of the workspace.


--- Page 20: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ellipse-Node.html ---

# Ellipse Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ellipse-Node.html#description)Description
Generates an ellipse shape based on input **UV** at the size specified by inputs **Width** and **Height**. The generated shape can be offset or tiled by connecting a [Tiling And Offset Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html). Note that in order to preserve the ability to offset the shape within the UV space the shape will not automatically repeat if tiled. To achieve a repeating dot effect first connect your input through a [Fraction Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html).
NOTE: This [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can only be used in the **Fragment** [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ellipse-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Width | Input | Float | None | Ellipse width  
Height | Input | Float | None | Ellipse height  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ellipse-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Ellipse_float(float2 UV, float Width, float Height, out float4 Out)
{
    float d = length((UV * 2 - 1) / float2(Width, Height));
    Out = saturate((1 - d) / fwidth(d));
}

```



--- Page 21: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html ---

# Flip Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html#description)Description
Flips the individual channels of input **In** selected by the [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html)'s parameters. Positive values become negative values and vice versa.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Dynamic Vector | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Red | Toggle | True, False | If true red channel will be flipped.  
Green | Toggle | True, False | If true green channel will be flipped. Disabled if **In** is Float.  
Blue | Toggle | True, False | If true blue channel will be flipped. Disabled if **In** is Vector 2 or smaller.  
Alpha | Toggle | True, False | If true alpha channel will be flipped. Disabled if **In** is Vector 3 or smaller.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 _Flip_Flip = float4(Red, Green, Blue, Alpha);

void Unity_Flip_float4(float4 In, float4 Flip, out float4 Out)
{
    Out = (Flip * -2 + 1) * In;
}

```



--- Page 22: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html ---

# Append Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#description)Description
Creates a new vector **Out** by combining the channels of input **A** followed by the channels of input **B**. Inputs **A** and **B** can have up to **three** channels.
**Out** can have **two** to **four** channels, depending on the combination of channels of the inputs.
Input **A** channels take priority over input **B** to combine up to a maximum of **four** in the output.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
A | Input | Dynamic | None | First input value  
B | Input | Dynamic | None | Second input value  
Out | Output | Dynamic | None | Combined vector from A and B  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#example-graph-usage)Example graph usage
In the following example, an **Append** node combines a **Vector 2** and a **Float**. The resulting output vector has 3 channels: the **X** and **Y** from the **Vector 2** , and the **X** from the **Float**.
Notice that with an Append node, you don't need to use a Split node to break up the Vector 2 into individual channels, then a Combine node to combine the 3 separate channels.
![An image of the Graph window that shows a Vector 2 node and a Float node with their outputs connected to the inputs of an Append node.](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-append-node-example.png)
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node for different inputs combinations.
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#vector2-and-float)Vector2 and Float
```
float3 Append_Out = float3( A.xy, B.x);

```

###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#float-and-vector3)Float and Vector3
```
float4 Append_Out = float4( A.x, B.xyz);

```

###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html#vector3-and-vector2)Vector3 and Vector2
```
float4 Append_Out = float4( A.xyz, B.x);

```



--- Page 23: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Contrast-Node.html ---

# Contrast Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Contrast-Node.html#description)Description
Adjusts the contrast of input **In** by the amount of input **Contrast**. A **Contrast** value of 1 will return the input unaltered. A **Contrast** value of 0 will return the midpoint of the input.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Contrast-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value  
Contrast | Input | Float | None | Contrast value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Contrast-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Contrast_float(float3 In, float Contrast, out float3 Out)
{
    float midpoint = pow(0.5, 2.2);
    Out = (In - midpoint) * Contrast + midpoint;
}

```



--- Page 24: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Any-Node.html ---

# Any Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Any-Node.html#description)Description
Returns true if any of the components of the input **In** are non-zero. This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Any-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Any-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Any_float4(float4 In, out float Out)
{
    Out = any(In);
}

```



--- Page 25: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html ---

# Combine Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html#description)Description
Creates new vectors from the four inputs **R** , **G** , **B** and **A**. Output **RGBA** is a **Vector 4** composed of inputs **R** , **G** , **B** and **A**. Output **RGB** is a **Vector 3** composed of inputs **R** , **G** and **B**. Output **RG** is a **Vector 2** composed of inputs **R** and **G**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
R | Input | Float | None | Defines red channel of output  
G | Input | Float | None | Defines green channel of output  
B | Input | Float | None | Defines blue channel of output  
A | Input | Float | None | Defines alpha channel of output  
RGBA | Output | Vector 4 | None | Output value as **Vector 4**  
RGB | Output | Vector 3 | None | Output value as **Vector 3**  
RG | Output | Vector 2 | None | Output value as **Vector 2**  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Combine_float(float R, float G, float B, float A, out float4 RGBA, out float3 RGB, out float2 RG)
{
    RGBA = float4(R, G, B, A);
    RGB = float3(R, G, B);
    RG = float2(R, G);
}

```



--- Page 26: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Slice.html ---

# Custom Render Texture Slice Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Slice.html#description)Description
Provides the slice index or cubemap face of the current **Custom Render Texture**. When a **Custom Render Texture** is a Cubemap, 3D texture, or 2D texture array, Shader Graph issues multiple draw calls to update each slice or face separately. Use this node to get the slice index or cubemap face.
For more information on Custom Render Textures, refer to the [Unity Manual](https://docs.unity3d.com/Manual/class-CustomRenderTexture.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Slice.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Texture Cube Face | Output | Float | None | The current face of the **Custom Render Texture** being updated. This value is an integer between 0 and 5 included.  
Texture Depth Slice | Output | Float | None | The current slice index of the **Custom Render Texture** being updated. This value is an integer between 0 and the volume depth of the texture.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Slice.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
_CustomRenderTextureCubeFace

```



--- Page 27: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Size.html ---

# Custom Render Texture Size Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Size.html#description)Description
Provides the size of the current **Custom Render Texture**.
For more information on Custom Render Textures, refer to the [Unity Manual](https://docs.unity3d.com/Manual/class-CustomRenderTexture.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Size.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Texture Width | Output | Float | None | Width of the **Custom Render Texture**.  
Texture Height | Output | Float | None | Height of the **Custom Render Texture**.  
Texture Depth | Output | Float | None | Volume depth of the **Custom Render Texture**. This is valid only for 3D texture and 2D texture array types.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Size.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
_CustomRenderTextureWidth

```



--- Page 28: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html ---

# Boolean Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html#description)Description
Defines a constant **Boolean** value in the [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html), although internally to the shader this is treated as a constant **float** value that is ether 0 or 1, similar to Shaderlab's [Toggle](https://docs.unity3d.com/ScriptReference/MaterialPropertyDrawer.html) property. Can be converted to a **Boolean** type [Property](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html) via the [Node's](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) context menu.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Toggle |  | Defines the output value.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html#generated-code-example)Generated Code Example
The following basic test code represents one possible outcome of this node with the Boolean value set to 0:
```
float _Boolean = 0;

```



--- Page 29: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Checkerboard-Node.html ---

# Checkerboard Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Checkerboard-Node.html#description)Description
Generates a checkerboard of alternating colors between inputs **Color A** and **Color B** based on input **UV**. The checkerboard scale is defined by input **Frequency**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Checkerboard-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Color A | Input | Color RGB | None | First checker color  
Color B | Input | Color RGB | None | Second checker color  
Frequency | Input | Vector 2 | None | Scale of checkerboard per axis  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Checkerboard-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Checkerboard_float(float2 UV, float3 ColorA, float3 ColorB, float2 Frequency, out float3 Out)
{
    UV = (UV.xy + 0.5) * Frequency;
    float4 derivatives = float4(ddx(UV), ddy(UV));
    float2 duv_length = sqrt(float2(dot(derivatives.xz, derivatives.xz), dot(derivatives.yw, derivatives.yw)));
    float width = 1.0;
    float2 distance3 = 4.0 * abs(frac(UV + 0.25) - 0.5) - width;
    float2 scale = 0.35 / duv_length.xy;
    float freqLimiter = sqrt(clamp(1.1f - max(duv_length.x, duv_length.y), 0.0, 1.0));
    float2 vector_alpha = clamp(distance3 * scale.xy, -1.0, 1.0);
    float alpha = saturate(0.5f + 0.5f * vector_alpha.x * vector_alpha.y * freqLimiter);
    Out = lerp(ColorA, ColorB, alpha.xxx);
}

```



--- Page 30: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/And-Node.html ---

# And Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/And-Node.html#description)Description
Returns true if both the inputs **A** and **B** are true. This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/And-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
A | Input | Boolean | None | First input value  
B | Input | Boolean | None | Second input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/And-Node.html#generated-code-example)Generated Code Example
```
void Unity_And(float A, float B, out float Out)
{
    Out = A && B;
}

```



--- Page 31: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html ---

# Color Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html#description)Description
Defines a constant **Vector 4** value in the shader using a **Color** field. Can be converted to a **Color** [Property Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html) via the [Node's](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) context menu. The value of the **Mode** parameter will also respected when generating the [Property](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html).
NOTE: In versions prior to 10.0, Shader Graph assumed that HDR colors from the Color Node were in gamma space. Version 10.0 corrected this behavior, and Shader Graph now interprets HDR colors in linear space. HDR Color nodes that you created with older versions maintain the old behavior, but you can use the [Graph Inspector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Internal-Inspector.html) to upgrade them. To mimic the old behavior on a new HDR Color node, you can use a [Colorspace Conversion Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html) to convert the HDR color from **RGB** to **Linear**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 4 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Color |  | Defines the output value.  
Mode | Dropdown | Default, HDR | Sets properties of the Color field  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float4 _Color = IsGammaSpace() ? float4(1, 2, 3, 4) : float4(SRGBToLinear(float3(1, 2, 3)), 4);

```



--- Page 32: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html ---

# Exponential Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html#description)Description
Returns the exponential value of input **In**. The exponential base can be switched between base-e and base 2 from the **Base** dropdown on the node.
  * **Base E** : Returns e to the power of input **In**
  * **Base 2** : Returns 2 to the power of input **In**


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Base | Dropdown | BaseE, Base2 | Selects the exponential base  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Base** mode.
**Base E**
```
void Unity_Exponential_float4(float4 In, out float4 Out)
{
    Out = exp(In);
}

```

**Base 2**
```
void Unity_Exponential2_float4(float4 In, out float4 Out)
{
    Out = exp2(In);
}

```



--- Page 33: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Built-In-Blocks.html ---

# Built In Blocks
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Built-In-Blocks.html#vertex-blocks)Vertex Blocks
| Name | Type | Binding | Description  
---|---|---|---|---  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Vertex-Position.png) | Position | Vector 3 | Object Space Position | Defines the absolute object space vertex position per vertex.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Vertex-Normal.png) | Normal | Vector 3 | Object Space Normal | Defines the absolute object space vertex normal per vertex.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Vertex-Tangent.png) | Tangent | Vector 3 | Object Space Tangent | Defines the absolute object space vertex tangent per vertex.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Vertex-Color.png) | Color | Vector 4 | Vertex Color | Defines vertex color. Expected range 0 - 1.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Built-In-Blocks.html#fragment-blocks)Fragment Blocks
| Name | Type | Binding | Description  
---|---|---|---|---  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Base-Color.png) | Base Color | Vector 3 | None | Defines material's base color value. Expected range 0 - 1.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-NormalTS.png) | Normal (Tangent Space) | Vector 3 | Tangent Space Normal | Defines material's normal value in tangent space.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-NormalOS.png) | Normal (Object Space) | Vector 3 | Object Space Normal | Defines material's normal value in object space.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-NormalWS.png) | Normal (World Space) | Vector 3 | World Space Normal | Defines material's normal value in world space.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Emission.png) | Emission | Vector 3 | None | Defines material's emission color value. Expects positive values.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Metallic.png) | Metallic | Float | None | Defines material's metallic value, where 0 is non-metallic and 1 is metallic.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Specular.png) | Specular | Vector 3 | None | Defines material's specular color value. Expected range 0 - 1.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Smoothness.png) | Smoothness | Float | None | Defines material's smoothness value. Expected range 0 - 1.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Ambient-Occlusion.png) | Ambient Occlusion | Float | None | Defines material's ambient occlusion value. Expected range 0 - 1.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Alpha.png) | Alpha | Float | None | Defines material's alpha value. Used for transparency and/or alpha clip. Expected range 0 - 1.  
![image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/Blocks-Fragment-Alpha-Clip-Threshold.png) | Alpha Clip Threshold | Float | None | Fragments with an alpha below this value are discarded. Expected range 0 - 1.


--- Page 34: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html ---

# Constant Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html#description)Description
Defines a **Float** of a mathematical constant value in the shader.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Mode | Dropdown | PI, TAU, PHI, E, SQRT2 | Sets output constant value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per constant type.
**PI**
```
float _Constant_PI = 3.1415926;

```

**TAU**
```
float _Constant_TAU = 6.28318530;

```

**PHI**
```
float _Constant_PHI = 1.618034;

```

**E**
```
float _Constant_E = 2.718282;

```

**SQRT2**
```
float _Constant_SQRT2 = 1.414214;

```



--- Page 35: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/All-Node.html ---

# All Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/All-Node.html#description)Description
Returns true if all components of the input **In** are non-zero. This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/All-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/All-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_All_float4(float4 In, out float Out)
{
    Out = all(In);
}

```



--- Page 36: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html ---

# Flipbook Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html#description)Description
Creates a flipbook, or texture sheet animation, of the UVs supplied to input **UV**. The amount of tiles on the sheet are defined by the values of the inputs **Width** and **Height**. The index of the current tile is defined by the value of the input **Tile**.
This node can be used to create a texture animation functionality, commonly used for particle effects and sprites, by supplying [Time](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html) to the input **Tile** and outputting to the UV input slot of a [Texture Sampler](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Node.html).
UV data is typically in the range of 0 to 1 starting from the bottom left of UV space. This can be seen by the black value at the bottom left corner of a UV preview. As flipbooks typically start from top left the parameter **Invert Y** is enabled by default, however you can change the direction of the Flipbook by switching the **Invert X** and **Invert Y** parameters.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Width | Input | Float | None | Amount of horizontal tiles  
Height | Input | Float | None | Amount of vertical tiles  
Tile | Input | Float | None | Current tile index  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Invert X | Toggle | True, False | If enabled tiles are iterated from right to left  
Invert Y | Toggle | True, False | If enabled tiles are iterated from top to bottom  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 _Flipbook_Invert = float2(FlipX, FlipY);

void Unity_Flipbook_float(float2 UV, float Width, float Height, float Tile, float2 Invert, out float2 Out)
{
    Tile = floor(fmod(Tile + float(0.00001), Width*Height));
    float2 tileCount = float2(1.0, 1.0) / float2(Width, Height);
    float base = floor((Tile + float(0.5)) * tileCount.x);
    float tileX = (Tile - Width * base);
    float tileY = (Invert.y * Height - (base + Invert.y * 1));
    Out = (UV + float2(tileX, tileY)) * tileCount;
}

```



--- Page 37: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html ---

# Graph Settings Tab
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html#description)Description
The **Graph Settings** tab on the [Graph Inspector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Internal-Inspector.html) makes it possible to change settings that affect the Shader Graph as a whole.
![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/GraphSettings_Menu.png)
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html#graph-settings-options)Graph Settings options
Menu Item | Description  
---|---  
**Precision** | Select **Single** or **Half** from the [Precision](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Precision-Modes.html) dropdown menu as the graph's default Precision Mode for the entire graph.  
**Preview Mode** | Select your preferred preview mode for a node that has a preview from the following options: 
  * **Inherit** : The Unity Editor automatically selects the preview mode to use.
  * **Preview 2D** : Renders the output of the Sub Graph as a flat two-dimensional preview.
  * **Preview 3D** : Renders the output of the Sub Graph on a three-dimensional object such as a sphere.

This property is available only when you selected a [Sub Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html).  
**Active Targets** | A list that contains selected targets. You can add or remove **Active Targets** by selecting the **Add (+)** and **Remove (−)** buttons, respectively.   
Shader Graph supports three targets: 
  * **Built-in** : Shaders for Unity’s [Built-In Render Pipeline](xref:um-render-pipelines).
  * **Custom Render Texture** : Shaders for updating [Custom Render Textures](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Render-Texture.html). 
  * **Universal** : Shaders for the [Universal Render Pipeline](xref:um-shaders-in-universalrp-reference).

The available properties displayed depend on the targets you have added to the list. Refer to the [Shader Material Inspector window properties](xref:um-shaders-in-universalrp-reference) for the respective **Materials** you select for the **Built-in** and **Universal** targets.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html#additional-resources)Additional resources
  * [Precision Modes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Precision-Modes.html)
  * [Example Custom Render Texture with Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Render-Texture-Example.html)
  * [Custom Editor block in ShaderLab reference](xref:um-sl-custom-editor)




--- Page 38: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html ---

# Gradient Noise Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html#description)Description
Generates a gradient, or [Perlin](https://en.wikipedia.org/wiki/Perlin_noise), noise based on input **UV**. The scale of the generated noise is controlled by input **Scale**. In terms of performance cost, Gradient Noise node can be slightly more computationally intensive than sampling a texture map.
You can also choose to use two different hashing methods for calculating the noise. As of Unity version 2021.2, the Gradient Noise node defaults to the **Deterministic** hash, to ensure consistent results for noise generation across platforms. Because the **UV** value is used as the seed for the noise generation, you can offset, scale, or distort the **UV** value to generate different noise patterns.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Scale | Input | Float | None | Noise scale  
Out | Output | Float | None | Output value in the range 0.0 to 1.0  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Hash Type | Dropdown | Deterministic, LegacyMod | Selects the hash function used to generate random numbers for noise generation.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 unity_gradientNoise_dir(float2 p)
{
    p = p % 289;
    float x = (34 * p.x + 1) * p.x % 289 + p.y;
    x = (34 * x + 1) * x % 289;
    x = frac(x / 41) * 2 - 1;
    return normalize(float2(x - floor(x + 0.5), abs(x) - 0.5));
}

float unity_gradientNoise(float2 p)
{
    float2 ip = floor(p);
    float2 fp = frac(p);
    float d00 = dot(unity_gradientNoise_dir(ip), fp);
    float d01 = dot(unity_gradientNoise_dir(ip + float2(0, 1)), fp - float2(0, 1));
    float d10 = dot(unity_gradientNoise_dir(ip + float2(1, 0)), fp - float2(1, 0));
    float d11 = dot(unity_gradientNoise_dir(ip + float2(1, 1)), fp - float2(1, 1));
    fp = fp * fp * fp * (fp * (fp * 6 - 15) + 10);
    return lerp(lerp(d00, d01, fp.y), lerp(d10, d11, fp.y), fp.x);
}

void Unity_GradientNoise_float(float2 UV, float Scale, out float Out)
{
    Out = unity_gradientNoise(UV * Scale) + 0.5;
}

```



--- Page 39: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting.html ---

# Custom Lighting
[![The Shader Graph Custom Lighting Sample: A collection of Shader Graph subgraphs that serve as building blocks for building user interface elements.](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/CustomLightingSample.png)](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/CustomLightingSample.png)
The Shader Graph Custom Lighting sample shows how you can create your own custom lighting in Shader Graph and provides dozens of example templates, shaders, and subgraphs to help you get started with your own custom lighting.
Documentation for this set of samples is broken into two pages:
  * [Lighting Models](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting-Lighting-Models.html)
  * [Components](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting-Components.html)


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting.html#limitations)Limitations
Before making your own custom lighting model in Shader Graph, be aware of the following limitations:
  * Customizable lighting is only intended to be used when the render type is set to Forward or Forward+ in the Render Asset.
When the render type is set to Deferred or Deferred+, it's not possible to control the lighting directly in an object’s shader, because the lighting occurs in a pass that is not directly connected to the object's shader.
If you need to customize lighting in deferred rendering context, you have to write code instead of using Shader Graph.
  * To support multiple light sources, you have to write a small amount of code.
For the main directional light, you can create custom lighting 100% in Shader Graph. However, the part of the graph that does multiple light calculations requires the use of a Custom Function node, because Shader Graph doesn’t support `For` loops.
The sample includes multiple examples of Additional Lights nodes, but if you want to create your own, you need to know a little bit of HLSL coding.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting.html#motivations)Motivations
There are two main reasons you might want to customize the lighting model in Shader Graph:
  * Improve rendering performance by leaving out one or more types of lighting calculations, sacrificing visual quality for rendering speed.
  * Make your lighting look different from the lighting that Unity already provides. For example, you might want your project to look like a watercolor painting, like it’s drawn with pen and ink, etc.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Custom-Lighting.html#examples)Examples
The sample includes the following subgraph examples in the Shader Graph node library:
  * Lighting / Light Models / Lit Basic
  * Lighting / Light Models / Lit Colorize
  * Lighting / Light Models / Lit Simple
  * Lighting / Light Models / Lit Toon
  * Lighting / Light Models / Lit URP


To get customized lighting with any of these subgraphs:
  1. Add the subgraph to an empty Shader Graph.
  2. Connect the Lit output port to the Base Color input port on the Unlit Master Stack.
  3. To allow the Unlit target to correctly support custom lighting models, make sure to set the Graph inspector as follows: 
     * Enable _Keep Lighting Variants_.
     * Disable _Default Decal Blending_ and _Default SSAO_.


Notice that each of the above subgraphs use the following:
  * The ApplyDecals subgraph to blend decal data with the original material properties.
  * The Debug Lighting and Debug Materials subgraph nodes to support the debug rendering modes (available in the Rendering Debugger window).
  * A subgraph from the Core Lighting Models category to define the behavior of the lighting itself.


While the ApplyDecals, DebugLighting, and DebugMaterials subgraph nodes aren’t strictly required, they are included in the lighting model subgraphs to enable these core engine features: decals and debug rendering modes. When these features are not in use, the ApplyDecals, DebugLighting, and DebugMaterials subgraph nodes don't add any performance cost to the shader overall. You can use them without worrying that you’re slowing down your project.
You can create any type of lighting that you want, but the above subgraphs show you a recommended pattern to illustrate how Unity expects custom lighting models to be defined.


--- Page 40: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html ---

# Invert Colors Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html#description)Description
Inverts the colors of input **In** on a per channel basis. This [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) assumes all input values are in the range 0 - 1.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Dynamic Vector | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Red | Toggle | True, False | If true red channel is inverted  
Green | Toggle | True, False | If true green channel is inverted. Disabled if input vector dimension is less than 2  
Blue | Toggle | True, False | If true blue channel is inverted. Disabled if input vector dimension is less than 3  
Alpha | Toggle | True, False | If true alpha channel is inverted. Disabled if input vector dimension is less than 4  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 _InvertColors_InvertColors = float4(Red, Green, Blue, Alpha);

void Unity_InvertColors_float4(float4 In, float4 InvertColors, out float4 Out)
{
    Out = abs(InvertColors - In);
}

```



--- Page 41: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Mode-Control.html ---

# Preview mode control
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Mode-Control.html#description)Description
This control enables you to manually select your preferred preview mode for a node that has a preview.
When you select **Inherit** in the Preview Mode Control, the Editor automatically selects the preview mode to use.
That decision is determined by either the type of the node you are previewing, the Sub Graph setting (if this node is in a Sub Graph) or other upstream nodes. To override the inheritance mode, select **Preview 2D** or **Preview 3D**.
This mode control functionality also applies to Sub Graph previews. See [Graph Settings menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Mode-Control.html#how-to-use)How to use
For nodes:
  1. Add a node which includes a preview.
  2. Select the node.
  3. In the Graph Inspector or Node Settings, find the Preview control.
  4. Select an option.


For SubGraphs:
  * Select a mode in the [Sub Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html) [Graph Settings](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Graph-Settings-Tab.html) menu.


![](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/previewmodecontrol.png)
Related [Preview node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html)


--- Page 42: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Replace-Color-Node.html ---

# Replace Color node
The Replace Color node replaces a color in the input with another color.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Replace-Color-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**In** | Input | Vector 3 | None | Sets the input you want to replace a color in. For example, a texture.  
**From** | Input | Vector 3 | Color | Sets the color to replace.  
**To** | Input | Vector 3 | Color | Sets the color to replace **From** with.  
**Range** | Input | Float | None | Sets the range around **From** to replace. For example, if you set **From** to (0, 0, 0) and **Range** to 0.1, Unity replaces colors from (0, 0, 0) to (0.1, 0.1, 0.1) with **To**.  
**Fuzziness** | Input | Float | None | Sets how much to soften the boundary between the replaced color and the rest of the colors.  
**Out** | Output | Vector 3 | None | The **In** input, with the **From** color replaced with the **To** color.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Replace-Color-Node.html#generated-code-example)Generated code example
The following example code represents one possible outcome of this node.
```
void Unity_ReplaceColor_float(float3 In, float3 From, float3 To, float Range, float Fuzziness, out float3 Out)
{
    float Distance = distance(From, In);

    // Use max to avoid division by zero
    Out = lerp(To, In, saturate((Distance - Range) / max(Fuzziness, 1e-5f)));
}

```



--- Page 43: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html ---

# Integer Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html#description)Description
Defines a constant **Float** value in the shader using an **Integer** field. Can be converted to a **Float** type [Property](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html) with a **Mode** setting of **Integer** via the [Node's](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) context menu.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Integer |  | Defines the output value.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float _Integer = 1;

```



--- Page 44: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders.html ---

# UGUI Shaders
[![The Shader Graph UGUI Shaders: A collection of Shader Graph subgraphs that serve as building blocks for building user interface elements.](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/UIToolsSample.png)](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/UIToolsSample.png)
The Shader Graph UGUI Shaders sample is a collection of Shader Graph subgraphs that serve as building blocks for building user interface elements. They speed up the process of building widgets, buttons, and backgrounds for the user interface of your project. Using these tools, you can build dynamic, procedural UI elements that don’t require any texture memory and scale correctly for any resolution screen.
In addition to the subgraphs, the sample also includes example buttons, indicators, and backgrounds built using the subgraphs. The examples show how the subgraphs function in context and help you learn how to use them.
We have two main objectives with this sample set:
  * Demonstrate Shader Graph’s ability to create dynamic, resolution-independent user interface elements in a wide variety of shapes and styles.
  * Make it easier and faster to create UI elements by providing a large set of UI-specific subgraph nodes that can be used as building blocks to speed up the creation process.


Using Shader Graph and UGUI, you can create user interface elements that are resolution independent, require zero texture memory, can be authored and edited directly in Shader Graph inside of Unity, automatically adapt to aspect ratio, and contain all visual states and behaviors. That’s a lot, so let’s unpack it!
  * **Resolution Independent** - These UI elements are procedurally-generated, so they look perfectly crisp whether displayed on a small smartphone screen or a 100 inch 8k TV. You can zoom in on them as close as you want and they’ll always be tack sharp.
  * **Zero Texture Memory** - The visuals for these UI elements are created using math, so they don’t rely on textures at all. That means they require zero texture memory.
  * **Authored In Shader Graph** - If you’re frustrated by the back and forth workflow of editing your UI images outside of Unity, chopping them up into textures, importing them, and then going back to make adjustments, you’ll be glad to hear that these UI elements are created entirely in Shader Graph, so there’s no export/import loop. Adjustments require simply changing shader parameters or re-wiring a few nodes.
  * **Automatically Adapt To Aspect Ratio** - By passing the width and height values of the assigned UI element into the shader, the shader can automatically adapt the visuals to fit that ratio. No more making different button shapes to fit different size buttons or fiddling with 9 slicing.
  * **Contain all visual states and behaviors** - One shader can contain all the information needed for a hover state, and active/inactive state, a pressed down state, etc, so you don’t need to manage multiple image assets for each button or widget.


This set of samples demonstrates how to use all of these advanced techniques for generating UI, and provides tools to make the process easier.
Documentation for this set of samples is broken into the following pages:
  * [Getting started](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-Getting-Started.html)
  * [Custom UI componenents](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-Custom-UI-components.html)
  * [Custom nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-Custom-nodes.html)
  * [Subgraph nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-Subgraph-nodes.html)
  * [Examples](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-Examples.html)
  * [How tos](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-How-tos.html)
    * [How to create a resolution-independent shape](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-How-tos-Res-indepenent.html)
    * [How to create a functioning button](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-How-tos-Button.html)
    * [How to make shapes that adapt to the aspect ratio of the UI element](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-How-tos-aspect-ratio.html)
  * [Notes on performance](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-UGUI-Shaders-Notes-on-performance.html)




--- Page 45: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radial-Shear-Node.html ---

# Radial Shear Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radial-Shear-Node.html#description)Description
Applies a radial shear warping effect similar to a wave to the value of input **UV**. The center reference point of the warping effect is defined by input **Center** and the overall strength of the effect is defined by the value of input **Strength**. Input **Offset** can be used to offset the individual channels of the result.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radial-Shear-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Center | Input | Vector 2 | None | Center reference point  
Strength | Input | Float | None | Strength of the effect  
Offset | Input | Vector 2 | None | Individual channel offsets  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radial-Shear-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_RadialShear_float(float2 UV, float2 Center, float Strength, float2 Offset, out float2 Out)
{
    float2 delta = UV - Center;
    float delta2 = dot(delta.xy, delta.xy);
    float2 delta_offset = delta2 * Strength;
    Out = UV + float2(delta.y, -delta.x) * delta_offset + Offset;
}

```



--- Page 46: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html ---

# Log Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html#description)Description
Returns the logarithm of input **In**. **Log** is the inverse operation to the [Exponential Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html).
For example, the result of a base-2 **Exponential** using an input value of 3 is 8.
![Two raised to the power of three = 2 x 2 x 2 = eight.](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/LogNodePage02.png)
Therefore the result of a base-2 **Log** using an input value of 8 is 3.
The logarithmic base can be switched between base-e, base-2 and base-10 from the **Base** dropdown on the node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Base | Dropdown | BaseE, Base2, Base10 | Selects the logarithmic base  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Base** mode.
**Base E**
```
void Unity_Log_float4(float4 In, out float4 Out)
{
    Out = log(In);
}

```

**Base 2**
```
void Unity_Log2_float4(float4 In, out float4 Out)
{
    Out = log2(In);
}

```

**Base 10**
```
void Unity_Log10_float4(float4 In, out float4 Out)
{
    Out = log10(In);
}

```



--- Page 47: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Simple-Noise-Node.html ---

# Simple Noise node
The Simple Noise node generates a pseudo-random value, also known as value noise, for each UV coordinate in the input **UV**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Simple-Noise-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**UV** | Input | Vector 2 | UV | The UV coordinates to input. For example UV coordinates, refer to [UV Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Nodes.html).  
**Scale** | Input | Float | None | How much to scale the size of the output. A higher value zooms out so there are more noise values in the same space. The default is 500.  
**Out** | Output | Float | None | The simple noise. The range of each value is between 0 and 1.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Simple-Noise-Node.html#hash-type)Hash Type
The **Hash Type** dropdown determines the hash function Unity uses to generate random numbers for the noise generation.
**Option** | **Description**  
---|---  
**Deterministic** | Uses a hash function that generates the same noise across different platforms. This is the default option.  
**Legacy Sine** | Uses a sine-based hash function. For most uses, **Deterministic** replaces **Legacy Sine**.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Simple-Noise-Node.html#generated-code-example)Generated code example
The following example code represents one possible outcome of this node.
```
inline float unity_noise_randomValue (float2 uv)
{
    return frac(sin(dot(uv, float2(12.9898, 78.233)))*43758.5453);
}

inline float unity_noise_interpolate (float a, float b, float t)
{
    return (1.0-t)*a + (t*b);
}

inline float unity_valueNoise (float2 uv)
{
    float2 i = floor(uv);
    float2 f = frac(uv);
    f = f * f * (3.0 - 2.0 * f);

    uv = abs(frac(uv) - 0.5);
    float2 c0 = i + float2(0.0, 0.0);
    float2 c1 = i + float2(1.0, 0.0);
    float2 c2 = i + float2(0.0, 1.0);
    float2 c3 = i + float2(1.0, 1.0);
    float r0 = unity_noise_randomValue(c0);
    float r1 = unity_noise_randomValue(c1);
    float r2 = unity_noise_randomValue(c2);
    float r3 = unity_noise_randomValue(c3);

    float bottomOfGrid = unity_noise_interpolate(r0, r1, f.x);
    float topOfGrid = unity_noise_interpolate(r2, r3, f.x);
    float t = unity_noise_interpolate(bottomOfGrid, topOfGrid, f.y);
    return t;
}

void Unity_SimpleNoise_float(float2 UV, float Scale, out float Out)
{
    float t = 0.0;

    float freq = pow(2.0, float(0));
    float amp = pow(0.5, float(3-0));
    t += unity_valueNoise(float2(UV.x*Scale/freq, UV.y*Scale/freq))*amp;

    freq = pow(2.0, float(1));
    amp = pow(0.5, float(3-1));
    t += unity_valueNoise(float2(UV.x*Scale/freq, UV.y*Scale/freq))*amp;

    freq = pow(2.0, float(2));
    amp = pow(0.5, float(3-2));
    t += unity_valueNoise(float2(UV.x*Scale/freq, UV.y*Scale/freq))*amp;

    Out = t;
}

```



--- Page 48: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready.html ---

# Production Ready Shaders
The Shader Graph Production Ready Shaders sample is a collection of Shader Graph shader assets that are ready to be used out of the box or modified to suit your needs. You can take them apart and learn from them, or just drop them directly into your project and use them as they are. The sample also includes a step-by-step tutorial for how to combine several of the shaders to create a forest stream environment.
The sample content is broken into the following categories:
Topic | Description  
---|---  
**[Lit shaders](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Lit.html)** | Introduces Shader Graph versions of the HDRP and URP Lit shaders. Users often want to modify the Lit shaders but struggle because they’re written in code. Now you can use these instead of starting from scratch.  
**[Decal shaders](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Decal.html)** | Introduces shaders that allow you to enhance and add variety to your environment. Examples include running water, wetness, water caustics, and material projection.  
**[Detail shaders](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Detail.html)** | Introduces shaders that demonstrate how to create efficient [terrain details](https://docs.unity3d.com/Manual/terrain-Grass.html) that render fast and use less texture memory. Examples include clover, ferns, grass, nettle, and pebbles.  
**[Rock](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Rock.html)** | A robust, modular rock shader that includes base textures, macro and micro detail, moss projection, and weather effects.  
**[Water](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Water.html)** | Water shaders for ponds, flowing streams, lakes, and waterfalls. These include depth fog, surface ripples, flow mapping, refraction and surface foam.  
**[Post-Process](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Post.html)** | Shaders to add post-processing effects to the scene, including edge detection, half tone, rain on the lens, an underwater look, and VHS video tape image degradation.  
**[Weather](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Weather.html)** | Weather effects including rain drops, rain drips, procedural puddles, puddle ripples, and snow.  
**[Miscellaneous](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Misc.html)** | A couple of additional shaders - volumetric ice, and level blockout shader.  
**[Forest Stream Construction Tutorial](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Production-Ready-Tutorial.html)** | A tutorial that describes how to combine multiple assets from this sample to create a forest stream.


--- Page 49: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Length-Node.html ---

# Length Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Length-Node.html#description)Description
Returns the length of input **In**. This is also known as magnitude. A vector's length is calculated with [Pythagorean Theorum](https://en.wikipedia.org/wiki/Pythagorean_theorem).
The length of a **Vector 2** can be calculated as:
![The square root of x squared plus y squared.](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/LengthNodePage02.png)
Where _x_ and _y_ are the components of the input vector. Length can be calculated for other dimension vectors by adding or removing components.
![The square root of \(x squared plus y squared plus z squared\).](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/LengthNodePage03.png)
And so on.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Length-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Float | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Length-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Length_float4(float4 In, out float Out)
{
    Out = length(In);
}

```



--- Page 50: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html ---

# Preview Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html#description)Description
This node enables you to inspect a preview at a specific point in a [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html). It does not modify any input values.
By default, the Editor automatically selects a preview mode. That decision is determined by both the type of the node you are previewing and other upstream nodes. With [Preview Mode Control](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Mode-Control.html), you can manually select your preferred preview mode.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Dynamic Vector | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Preview_float4(float4 In, out float4 Out)
{
    Out = In;
}

```



--- Page 51: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html ---

# Port
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html#description)Description
A **Port** defines an input or output on a [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html). Connecting [Edges](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) to a **Port** allows data to flow through the Shader Graph node network.
Each **Port** has a [Data Type](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) which defines what edges can be connected to it. Each data type has an associated color for identifying its type.
Only one edge can be connected to any input **Port** but multiple edges can be connected to an output **Port**.
You can open a contextual [Create Node Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html) by dragging an edge from a **Port** with left mouse button and releasing it in an empty area of the workspace.
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html#default-inputs)Default Inputs
Each **Input Port** , a **Port** on the left side of a node implying that it is for inputting data into the node, has a **Default Input**. This appears as a small field connected to the **Port** when there is no edge connected. This field will display an input for the ports data type unless the **Port** has a [Port Binding](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port-Bindings.html). If a **Port** does have a port binding the default input field might display a special field, such as a dropdown for selecting UV channels, or just a label to help you understand the intended input, such as coordinate space labels for geometry data.


--- Page 52: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Modulo-Node.html ---

# Modulo Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Modulo-Node.html#description)Description
Returns the remainder of dividing input **A** by input **B**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Modulo-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Modulo-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Modulo_float4(float4 A, float4 B, out float4 Out)
{
    Out = fmod(A, B);
}

```



--- Page 53: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html ---

# Hue Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html#description)Description
Offsets the hue of input **In** by the amount of input **Offset**. The unit of the offset can be set with the parameter **Range**. **Offset** in **Degrees** is in the range -180 to 180. In **Radians** it is -Pi to Pi.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value  
Offset | Input | Float | None | Amount to offset hue  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Range | Dropdown | Degrees, Radians | The unit used for the input **Offset**  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Base** mode.
**Degrees**
```
void Unity_Hue_Degrees_float(float3 In, float Offset, out float3 Out)
{
    float4 K = float4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    float4 P = lerp(float4(In.bg, K.wz), float4(In.gb, K.xy), step(In.b, In.g));
    float4 Q = lerp(float4(P.xyw, In.r), float4(In.r, P.yzx), step(P.x, In.r));
    float D = Q.x - min(Q.w, Q.y);
    float E = 1e-10;
    float3 hsv = float3(abs(Q.z + (Q.w - Q.y)/(6.0 * D + E)), D / (Q.x + E), Q.x);

    float hue = hsv.x + Offset / 360;
    hsv.x = (hue < 0)
            ? hue + 1
            : (hue > 1)
                ? hue - 1
                : hue;

    float4 K2 = float4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    float3 P2 = abs(frac(hsv.xxx + K2.xyz) * 6.0 - K2.www);
    Out = hsv.z * lerp(K2.xxx, saturate(P2 - K2.xxx), hsv.y);
}

```

**Radians**
```
void Unity_Hue_Radians_float(float3 In, float Offset, out float3 Out)
{
    float4 K = float4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    float4 P = lerp(float4(In.bg, K.wz), float4(In.gb, K.xy), step(In.b, In.g));
    float4 Q = lerp(float4(P.xyw, In.r), float4(In.r, P.yzx), step(P.x, In.r));
    float D = Q.x - min(Q.w, Q.y);
    float E = 1e-10;
    float3 hsv = float3(abs(Q.z + (Q.w - Q.y)/(6.0 * D + E)), D / (Q.x + E), Q.x);

    float hue = hsv.x + Offset;
    hsv.x = (hue < 0)
            ? hue + 1
            : (hue > 1)
                ? hue - 1
                : hue;

    // HSV to RGB
    float4 K2 = float4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    float3 P2 = abs(frac(hsv.xxx + K2.xyz) * 6.0 - K2.www);
    Out = hsv.z * lerp(K2.xxx, saturate(P2 - K2.xxx), hsv.y);
}

```



--- Page 54: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html ---

# Feature Examples
The Shader Graph Feature Examples sample content is a collection of Shader Graph assets that demonstrate how to achieve common techniques and effects in Shader Graph. The goal of this sample pack is to help users see what is required to achieve specific effects and provide examples to make it easier for users to learn.
The sample content is broken into the following categories:
  * **Blending Masks** - these samples generate masks based on characteristics of the surface - such as height, facing angle, or distance from the camera.
  * **Custom Interpolator** - here we show how to use the Custom Interpolator feature in Shader Graph to move calculations from the fragment stage to the vertex stage to save performance.
  * **Detail Mapping** - techniques for adding additional detail to a surface that isn’t contained in the base set of texture maps.
  * **Procedural Noise and Shapes** - methods for creating shapes or patterns that use math instead of texture samples.
  * **Shader Graph Feature Examples** - examples of using specific Shader Graph features - such as the Custom Code node or the Custom Interpolator
  * **UV Projection** - methods of creating texture coordinates to achieve specific effects such as parallax occlusion mapping, or triplanar projection
  * **Vertex Animation** - techniques for adjusting the position of the vertices to create effects such as waves, animated flags, or camera-facing billboards.
  * **Particles** - shows how a full-featured particle system can be built using just Shader Graph
  * **Conditions** - demonstrates branching based on graphics quality setting and based on the active render pipeline.
  * **Custom Lighting** - shows how Shader Graph can be used to build custom lighting models - including PBR, simple, and cel shading.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#blend-masks)Blend Masks
A major part of creating shaders is determining where specific effects should be applied. This is done by creating a mask and then using the mask to separate areas where the effect should be applied versus where it should not be applied. This set of samples provides examples of various methods of creating these masks.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#altitude-mask)Altitude Mask
The Altitude Mask is black below the minimum altitude, transitions from black to white between the minimum and maximum altitudes, and then stays white above the maximum altitude. You can use the AltitudeMask subgraph to create this effect.
The Altitude Mask example shows how to use the Altitude Mask subgraph in the shader to blend between two materials. Below the minimum altitude, the cobblestones material is used. Between minimum and maximum, the materials blend from cobblestones to gold, and then above the maximum, the gold material is used.
You can use the Falloff Type dropdown on the Altitude subgraph node to select the type of blend ramp to use. Linear will make the mask a direct line from minimum to maximum, while Smoothstep will create smooth transitions using a more S shaped curve.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#angle-mask)Angle Mask
The Angle Mask uses the direction that a surface is facing to determine if the mask should be black or white. If the surface is pointing in the direction of the given input vector, the mask is white. If it’s pointing away from the given vector, the mask is black.
The Angle Mask example uses the AngleMask subgraph to generate a mask, and then the mask is used to blend between the cobblestones material and a white, snow-like material.
In this example, the AngleMask subgraph node’s MaskVector input is set to 0,1,0 - which is a vector pointing in the up direction (positive Y). When the object’s surface is pointing in that direction, the mask is white. When the surface is pointing away from that direction, the mask is black.
The Max and Min input values on the AngleMask subgraph are used to control the falloff of the mask. Both values should use numbers between zero and one. When the Max and Min values are close together (0.5 and 0.48 for example), the falloff will be sharper. When they’re farther apart (0.8 and 0.3 for example), the falloff will be more gradual and blurry. When Max and Min are closer to a value of 1, the surface direction must match the MaskVector much more closely for the mask to be white. When Max and Min are closer to a value of zero, the mask will be white even with a larger difference between the surface direction and the MaskVector.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#camera-distance-mask)Camera Distance Mask
The Camera Distance Mask uses the distance from the camera location to the object’s surface to determine if the mask should be black or white. When the camera is close to the surface, the mask is black and when it’s further away, the mask is white.
In this example, we apply the cobblestones material when the camera is close to the object and as the camera moves away we blend to the gold material.
The Start Distance and Length values on the CameraDistanceMask subgraph control how the mask functions. The Start Distance value controls where the mask starts the transition from black to white. In this case, it’s set to 2 meters - which means that between 0 and 2 meters, the mask will be black. The Length value controls how long the transition is between black and white. In this case, it’s also set to 2 meters, so from a 2 meter distance to a 4 meter distance the mask will transition from black to white. Any distance beyond 4 meters will create a white mask.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#height-mask)Height Mask
The Height Mask uses the material height data of two materials to blend them together, creating a much more realistic looking intersection between them. Instead of fading between two materials, we can apply one material in the cracks and crevices of the other.
In this example, we use U texture coordinate as a smooth gradient mask, and then modify the mask using the heights of the two materials. Instead of a smooth blend, we end up with the gold material being applied in the lower areas of the cobblestones first and then gradually rising until just the tops of the cobblestones show before being replaced completely by the gold.
In order for this effect to work correctly, one or both of the materials need good height data. This type of a transition works best on materials with varying heights - like the cobblestones. Materials that are mostly flat won’t generate interesting effects with this technique.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#custom-interpolator)Custom Interpolator
The Custom Interpolator feature in Shader Graph allows you to do any type of calculation in the Vertex Stage and then interpolate the results to be used in the Fragment Stage. Doing calculations in the Vertex Stage can give a major performance boost since math is only done once per vertex instead of for every pixel.
However, per-vertex calculations can cause artifacts as illustrated in the Artifacts example. Be careful to only do math with low-frequency variations to avoid these artifacts.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#interpolation-artifacts)Interpolation Artifacts
This example shows the types of artifacts that can occur when we do math in the vertex stage. In order to be smooth, lighting needs to be calculated at each pixel - but here we’re doing the calculations per-vertex instead and then interpolating the results to the pixels. The interpolation is linear, so we don’t get enough accuracy and the result looks angular and jagged instead of smooth - especially on the specular highlight.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#interpolation-savings)Interpolation Savings
This example demonstrates a use case where custom interpolators can be highly beneficial. When creating shaders, it's common to tile and offset UVs multiple times. This behavior can become quite costly, especially when scrolling UVs on a fairly large object. For instance, consider a water shader where the water plane covers most of the terrain. Tiling the UVs in the fragment stage means performing the calculation for every pixel the water plane covers. One way to optimize this is to use custom interpolators to calculate the UVs in the vertex stage first and then pass the data to the fragment stage. Since there are fewer vertices than pixels on the screen, the computational cost will be lower. In this case, unlike the Custom Interpolator NdotL example, we do the samping after so that the rendering results are almost unnoticeable.
When "InFragStage" is set to "true", the UVs calculated in the fragment stage are used. When "InFragStage" is set to "false", the UVs are scrolled in the vertex stage. In this case, scrolling UVs in either the vertex or fragment stages won't cause a noticeable difference in the rendering result. However, it's much more cost-friendly to perform the calculations in the vertex stage and pass the data using custom interpolators.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#detail-mapping)Detail Mapping
Detail Mapping refers to a set of techniques where additional detail is added to the surface of a model that is not contained in the model’s base set of textures. These techniques are used when the camera needs to get closer to a model than the resolution of the textures would typically allow, or when the object is so large that the resolution of the base textures is insufficient.
In the three Detail Mapping examples, we’re using a texture packing format for our detail texture called NOS - which is short for Normal, Occlusion, Smoothness. This indicates that the Normal is stored in the red and green channels of the texture, the ambient occlusion is stored in the blue channel, and the smoothness is stored in the alpha channel. Packing the data together in this way allows us to get maximum use from our single detail texture - and we can add detail to the color, normal, smoothness, and AO with just a single texture sample. To simplify the process, we use the UnpackDetailNOS subgraph to sample the NOS detail texture and unpack the data.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#detail-map-color)Detail Map Color
For the Color Detail Map example, we simply multiply the Albedo output of the UnpackDetailNOS subgraph with the base color texture. The NOS texture format stores ambient occlusion data in the blue channel of the detail texture - and this occlusion data is what the UnpackDetailNOS subgraph passes to the Albedo output port. So for color detail, we’re just multiplying our base color by the detail AO.
Notice that the effect is quite subtle. In the past, when detail mapping was a new technique, most surfaces used only color textures - so color detail mapping was the main technique used. Now that materials use normals, smoothness, occlusion, etc, it works much better to use detail mapping for all of the maps instead of just the color.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#detail-map-normal)Detail Map Normal
For the Detail Map Normal example we combine the Normal output of the UnpackDetailNOS subgraph with the base normal map. Here we’re using the Normal Blend node to combine the two normals together and we have the Reoriented mode selected for best quality.
Notice that the Detail Map Normal example is significantly more impactful than the Detail Map Color example. The detail normals are changing the perceived shape of the surface - which has a very strong effect on the lighting, whereas the Color Detail example is only changing the color - which is less effective. This indicates that if you can only apply detail to one of the textures in your material, the normal is the most effective one to add detail to.
If you wanted to make this effect slightly cheaper to render, you could set the Normal Blend node to the Default mode instead (which uses the Whiteout normal blend technique instead). For another optimization, you could also set the Quality dropdown on the UnpackDetailNOS subgraph to Fast instead of Accurate. Both of these optimizations together would reduce the number of instructions required to render the effect. The results would be slightly less accurate, but this might not be noticeable. Try it out in your own shaders and see. If you can’t tell the difference, use the cheaper techniques for better performance!
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#detail-map-full)Detail Map Full
The Detail Map Full example adds detail to the color, normal, ambient occlusion, and smoothness components of the material - so we’re adding additional detail to almost all of the material components. This is the most effective way to add detail to a surface, but also a little more expensive than the Color or Normal examples.
Take special note of the way that we’re blending each of the outputs of the UnpackDetailNOS subgraph with their counterparts in the main material. For color, we’re using Multiply - so the detail color data darkens the base color. For Normal, we’re using the Normal Blend node. For Ambient Occlusion, we’re using the Minimum node, so the result is whichever result is darker. We’re using the Minimum node instead of Multiply to prevent the ambient occlusion from getting too dark. And finally, for the smoothness, we’re using Add. This is because the Smoothness data is in the -0.5 to 0.5 range and adding this range to the base smoothness acts like an overlay with darks darkening and brights brightening.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#procedural-noise-and-shapes)Procedural Noise and Shapes
In shaders, the term “procedural” refers to techniques that generate shapes and patterns using a series of math formulas - computed in real-time - instead of sampling texture maps. Procedural noise patterns and shapes have various advantages over texture maps including using no texture memory, covering infinite surface area without repetition or tiling, and being independent of texture resolution.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#hex-grid)Hex Grid
A Hexagon grid is useful for all types of projects so we decided to include one in the examples. In the example the Grid output port of the HexGrid subgraph is simply connected to the Base Color of the Master Stack. The HexGrid subgraph also has an EdgeDistance output port and a TileID output port. The Edge Distance output provides a signed distance field value that represents the distance to the nearest hexagon edge. So the pixels right in the center of each hexagon are white and then the closer you get to hexagon edges, the darker the pixels become. The TileID output port provides a different random value for each tile.
The HexGrid subgraph node also has some useful input ports. The UV input allows you to control the UV coordinates that are used to generate the pattern. The Scale input gives you control over the dimensions of the effect on both the X and Y axis. Finally, the Line Width input controls the thickness of the grid outlines. Line Width only applied to the Grid output and does not change the output of Edge Distance or TileID.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#procedural-brick)Procedural Brick
The Procedural Brick example shows how a brick pattern can be generated using pure math and no texture samples. If you’re developing on a platform that is fast at doing math but slow at texture samples, sometimes it can be much more performant to generate patterns like bricks procedurally rather than by sampling textures. Another advantage is that the variations in the brick patterns don’t repeat - so if you need a pattern to cover a large area without any repetition, procedural generation might be your best option.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#sdf-shapes)SDF Shapes
Shader Graph comes with a set of nodes for creating shapes procedurally (Ellipse, Polygon, Rectangle, Rounded Rectangle, Rounded Polygon) but frequently developers find that a signed distance field of the shape is more useful than the shape itself. SDFs can be joined together in interesting ways and give developers more flexibility and control in generating results than just having the shape itself. This is why we’ve included these SDF shapes in the examples.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#shader-graph-feature-examples)Shader Graph Feature Examples
The Shader Graph tool has several more advanced features - such as port defaults and Custom Interpolators - that can be tricky to set up. This section contains examples for those features to help users know what is required to set up and use these more advanced features.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#subgraph-dropdown)Subgraph Dropdown
When creating a subgraph node, it’s possible to add a dropdown control to allow users to make a selection. This is useful when there are several different methods of achieving a similar result and you want to allow the user of the subgraph to select which method to use. This example illustrates how to add a dropdown box to your subgraph.
After creating your subgraph asset, open it in the editor and open the Blackboard panel. Click the plus icon at the top and select Dropdown at the bottom of the list of parameter types. Now give your dropdown a name. Once the dropdown parameter is named, select it and open the Graph Inspector. Here you can control the number and names of the options in the dropdown list. Use the plus and minus icons at the bottom of the list to add and remove items. And click on individual items in the list to change their names. Once you have the number of items you want in the list, go back to the Blackboard and drag and drop your Blackboard parameter into the graph. It will appear as a node with input ports to match the list items you created in the Graph Inspector. For each of the input ports, create a graph that generates the results that you want for that option. The dropdown node acts as a switch to switch between the inputs depending on what is selected with the dropdown.
When the subgraph is added to a graph, the user will be able to select an option from the dropdown and the graph will use the branch of the graph that has been selected. Since the branch is static, only the selected branch will be included in the shader at runtime so no additional shader variants will be generated and no performance penalty will be incurred.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#subgraph-port-defaults)Subgraph Port Defaults
You can use the Branch on Input Connection node to set up defaults for the input ports of your subgraphs and even create large graph trees to use if nothing is connected to a specific input port. The Subgraph Port Defaults example shows how to do that.
After creating your subgraph asset, open it in the editor and open the Blackboard panel. Click the plus icon at the top and select a data type. In our example, we selected a Vector 2 type because we’re making an input port for UV coordinates. Once you’ve selected a type, give your parameter a name. We named ours UV. Before adding the parameter to your graph, select it and open the Graph Inspector. In the Graph Inspector, check the “Use Custom Binding” checkbox and give the parameter a Label. This is the name that will show up as connected to the port when no external wires are connected. Now, drag and drop your parameter from the Blackboard into the graph. Next, hit the spacebar and add a Branch on Input Connection node. The node can be found in the Searcher under Utilities->Logic. This node will allow you to set up a default input value or graph branch to use when nothing is connected to the input port. Connect your input parameter’s output port to the Input and Connected input ports of the Branch on Input Connection node. This will allow the input port to function correctly when a wire is connected to it. Now you can connect a node or node tree to the NotConnected input port. Whatever is connected here will be what gets used when nothing is connected to this subgraph’s input port. In our example, we’ve connected the UV node and used the Swizzle node so only the X and Y coordinates are used. So with this setup, UV0 will be used if nothing is connected to the input port.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#uv-projection)UV Projection
UV coordinates are used to translate the 3d surface area of models into 2d space that can be used to apply texture maps. This section contains a set of examples for creating, manipulating, and applying UV coordinates to achieve many different types of effects.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#flipbook)Flipbook
A flipbook is an effect where a series of frames is played back in sequence. The frames are arranged in a grid pattern on a texture map. Shader Graph has a built-in node that generates the UVs required to jump from one frame to the next on the texture.
In this example, we show how to use Shader Graph’s built-in Flipbook node to create an animated effect. We also show that you can use a pair of Flipbook nodes to set up an effect that blends smoothly from one frame to the next instead of jumping.
Notice that in the Blackboard, we’ve exposed a Texture parameter for selecting a flipbook texture, Rows and Columns parameters to describe the layout of the flipbook texture, a Speed parameter to control the playback rate of the frames, and a Flip Mode dropdown.
With the Flip Mode dropdown, you can select to Flip from one frame to the next, or to Blend between frames. Notice that if you select the Blend option, the playback appears much more smooth even though the frame rate remains the same. Using this Blend mode is a good way to improve the appearance of the effect and make it feel less choppy, even if the frame rate is low.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#flow-mapping)Flow Mapping
Flow Mapping is a technique that creates the illusion of flowing movement in a texture. It’s achieved by warping the texture coordinates along a specific flow direction over time in two separate phases. When the warping of the first phase becomes too severe, we blend to the second phase which is not yet warped and then warp that while removing the warping from the first phase while it is not displayed. We can blend back and forth between the two phases over and over to create the illusion of motion.
In the example, we’re using the UVFlowMap subgraph which does the main work of the effect. We give it a Flow Map - which is the direction to push the movement. In our case we’ve used a texture (similar to a normal map) to specify the direction. Then we give it a Strength value - which controls the distance that the UVs get warped. Flow Time can be as simple as just the Time node, but you can also connect a Flow Map Time subgraph which varies the time in different areas to break up the strobing effect. The UV input controls how the texture is applied. Notice that we’re using a Tiling And Offset node here to tile the texture 8 times. And finally the Offset value controls the midpoint of the stretching effect. The default value of 0.5 means that each of the phases starts out half stretched in the negative direction, moves to unstretched, and then moves to half stretched in the positive direction. This will give the best results in most cases.
In our example, we have exposed a Temporal Mode dropdown which illustrates the usefulness of the Flow Map Time subgraph. When Temporal Mode is set to Time Only, we’re only using Time as the Flow Time input. There is a noticeable strobing effect where the entire model appears to be pulsing in rhythm. This is because the blending between phase 1 and phase 2 is happening uniformly across the whole surface. When we set Temporal Mode to Flow Map Time, we’re using the Flow Map Time subgraph as the Flow Time input. The Flow Map Time subgraph breaks up the phase blending into smooth gradients across the surface so that it’s non-uniform and removes the strobing effect.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#interior-cube-mapping)Interior Cube Mapping
Interior Cube Mapping is a technique that creates the illusion of building interiors as seen through windows where no interior mesh exists. The effect can be used to make very simple exterior building meshes appear to have complex interiors and is much cheaper than actually modeling interiors.
In our example, the UVInteriorCubemap subgraph generates the direction vector that we need for sampling our cube map. The cube map creates the illusion of the interiors. And then the rest of the graph creates the exterior building and windows.
The UVInteriorCubemap subgraph has inputs for specifying the number of windows and controlling whether or not to randomize the walls of the cube map. The randomization rotates the walls of the cube map so that each interior has different walls on the sides and back. There is also a dropdown for controlling whether the projection is happening in object space or in UV space.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#lat-long-projection)Lat Long Projection
The Lat Long Projection example demonstrates the math required to use a texture map in the Latitude Longitude format. Many high dynamic range environment images are stored in this format so it’s useful to know how to use this type of image. You can tell an image is in LatLong format because it has a 2 to 1 aspect ratio and usually has the horizon running through the middle.
In our example, we’re using the UVLatLong subgraph. This node generates the UV coordinates needed to sample a texture map in the LatLong format. By default, the UVLatLong subgraph uses a reflection vector as input - so the result acts like a reflection on the surface of your model. But if you wanted the result to be stuck to the surface instead, you could use the Normal Vector.
If you select the Sample Texture 2D node and open the Graph Inspector, notice that the Mip Sampling Mode is set to Gradient. With that setting, the Sample Texture 2D node has DDX and DDY input ports - which we have connected to the DDX and DDY nodes. We’re doing this because the texture coordinates generated for the LatLong projection have a hard seam where the left and right sides of the projection wrap around and come together. If we were to set the Mip Sampling Mode to Standard instead, we would end up with a hard seam where the texture sampler failed because there is a large discontinuity in the mip values of the texture coordinates. The Gradient Mip Sampling Mode allows us to manually calculate our own mip level with the DDX and DDY nodes instead of allowing the sampler to do it.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#mat-cap-sphere-mapping)Mat Cap (Sphere Mapping)
The Mat Cap Material example demonstrates the math required to project a sphere map onto a surface. This effect is often called a Mat Cap - or material capture, because you can represent the properties of a material - like reflections or subsurface scattering - in the way the texture is created. Some 3d sculpting software uses MatCap projection to render objects. You can tell that a texture is a sphere map (or MatCap) because it looks a bit like a picture of a chrome ball. Sphere maps are the cheapest form of reflection - both in texture memory and in the low cost of math. But they’re not accurate because they always face the camera.
In our example, we’re using the UVSphereMap subgraph to generate the texture coordinates to sample the sphere map. The subgraph has an input for the surface normal - and you can use the dropdown to select the space that the normal is in. By default, the Vertex Normal is used, but you could also connect a normal map to it if you wanted to give the surface more detail.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#parallax-mapping)Parallax Mapping
There are many techniques that attempt to add more detail to the shape of a surface than is actually represented in the geometry of the surface. The Parallax Mapping example demonstrates three of these examples, and you can select which example to display with the Bump Type dropdown box in the material.
##### Normal Only
This technique is the cheapest and most common. It uses a normal map to change the apparent shape of the surface - where each pixel in the map represents the direction that the surface is facing at that point. Because there is no offsetting of the surface happening, this technique also looks fairly flat compared to the other two.
##### Parallax
Parallax Mapping samples a height map and then uses the value to offset the UV coordinates based on their height relative to the view direction. This causes parallax motion to occur on the surface and makes the surface feel like it has actual depth. However, when seen at steep angles, the effect often has artifacts. Where there are steep changes in the height map, there are visible stretching artifacts.
##### Parallax Occlusion
Parallax Occlusion Mapping samples a height map multiple times (based on the number of Steps) in a path along the view vector and reconstructs the scene depth of the surface. It uses this depth information to derive UV coordinates for sampling the textures. This process is expensive - especially with a high number of Steps, but can be made cheaper by creating a mask to reduce the number of Steps based on the camera distance and angle of the surface. Our example illustrates this technique.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#triplanar-projection)Triplanar Projection
Triplanar projection projects a texture onto the surface of a model from the front, side, and top. It’s useful when you want to apply a texture but the model doesn’t have good UV coordinates, or when the UVs are laid out for something else. It’s also useful when you want to project the same texture or material on many objects in close proximity and have the projection be continuous across them.
There are several methods for projecting a texture onto a surface. Our example shows four of them and you can select the method you want to see using the Projection Type dropdown in the material. They’re in order from most expensive to least.
##### Triplanar Texture projection
The Triplanar Textures technique uses the built-in Triplanar node in Shader Graph. This node samples each of your textures three times - for the top, front, and side projections and then blends between the three samples. This technique is the nicest looking since it blends between the samples, but it’s also the most expensive.
##### Biplanar Texture projection
This is a clever optimization to triplanar projection that uses two texture samples instead of three. The shader figures out which two faces are most important to the projection and only samples those two instead of all three. On most platforms, it will be cheaper than Triplanar Textures, but more expensive than Triplanar UVs. Depending on the textures you’re sampling, you may notice a small singularity artifact at the corner where the three faces come together.
##### Triplanar UV projection
The Triplanar UVs technique uses the UVTriplanar subgraph to project the UV coordinates from the top front and side and then use those to sample the textures only one time instead of three. Because it’s only sampling each texture one time, this technique is cheaper. The UV coordinates can’t be blended like the textures can - so this technique has hard seams where projections come together instead of blending like the Triplanar Textures technique. However, these seams aren’t very noticeable on some materials, so this may be an acceptable alternative if you need to do triplanar projection more cheaply.
Notice that the normal map needs to be plugged into the UVTriplanarNormalTransform node when using this technique in order to get the normals transformed correctly.
##### UV
This option just applies the textures using standard UV coordinates. It’s here so that you can easily compare it with the other two techniques.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#vertex-animation)Vertex Animation
Generally, we think of shaders as changing the color and appearance of pixels. But shaders can also be applied to vertices - to change the position of the points of a mesh. The model’s vertices can be manipulated by a shader to create all sorts of animated effects - as shown in this section.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#animated-flag)Animated Flag
This example shows a simple method for making a flag that ripples in the wind. The effect centers around the Sine node - which is what creates the rippling motion. We take the X position of the vertices and multiply them by a value that controls the length of the waves. We multiply that by Time and then pass that into the Sine node. Finally, we multiply the result of the Sine wave with a mask that goes from 0 at the point where the flag attaches to the pole, 1 at the tip of the flat where the effect should be strongest. The result is a simple rippling flag.
You could add additional detail to this effect if you combined several different sine waves that move at different speeds and wavelengths to vary and randomize the results. But something as simple as this example may be all that is needed if your flag is seen at a distance.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#bend-deformer---grass)Bend Deformer - Grass
This example shows the math required to bend a rectangle-shaped strip in an arc shape without changing its length. This can be used for animating blades of grass. The BendDeformer subgraph adjusts both the position and the normal of the vertices - so we get proper lighting on the updated shape.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#billboard)Billboard
The billboard example illustrates the math that we use to make a flat plane face the camera. Notice that the Billboard subgraph has a dropdown that allows us to select the initial direction that our plane is facing. Selecting the correct option here will ensure that our plane turns toward the camera correctly and not some other direction.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#gerstner-wave)Gerstner Wave
In this example, we use several instances of the GerstnerWave subgraph to animate waves in our mesh. The GerstnerWave subgraph does the math required to realistically simulate the movement of a single wave. Notice that each of the three instances has a different direction, wave length, and wave height. Combining these three different wave sizes together creates a really nice-looking wave simulation. The Offset values are added together and then added to the Position. The normals are combined using the Normal Blend node and then used directly as the Normal.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#particles)Particles
This example shows that it’s possible to create a simple particle system using nothing but Shader Graph! This method of creating particles is cheap because it’s done 100% on the GPU and almost all of the shader work happens in the vertex shader. This shader is not intended as a replacement for any of the other particle systems in Unity, but simply as an illustration of what’s possible to do with just Shader Graph alone. It could potentially be cheaper to make simple particle effects using this shader than with other methods. It’s definitely not as powerful or as full-featured as something made with VFX Graph, for example.
We start by creating a stack of planes where each plane in the stack has a slightly different vertex color. We use this value as an ID to differentiate each plane in the stack. This sample set comes with 3 stacks of planes that can be used. One with 25 planes, one with 50 planes, and one with 100 planes.
> Note that most particle systems dynamically generate particles based on the number that the system needs, but we’re using static geometry, so we’re locked in to using the number of planes in the geometry we choose. If the system we create with the material parameters requires more particles, the only way to fix it is to swap out the mesh that we’re using - so this is one major downside to this method.
We use the Billboard subgraph to make all of the planes face the camera and we use the Flipbook node to add an animated effect to the particles. We also add gravity and wind to control the movement of the particles. In the pixel shader, we expose control over the opacity and even fade out particle edges where they intersect with other scene geometry.
Here’s a description of the exposed material parameters that control the appearance and behavior of the particles:
Emitter Dimensions - controls the size of the particle emitter in X,Y, and Z. Particles will be born in random locations within the volume specified by these dimensions.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#color)Color
This is a color value that gets multiplied by the FlipbookTexture color. The StartColor blends to the EndColor throughout the lifetime of the particle. The alpha value of the color gets multiplied by the alpha value of the FlipbookTexture to contribute to the opacity of the particles. **Start Color** - the color multiplier for the particle at the beginning of its life **EndColor** - the color multiplier for the particle at the end of its life
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#opacity)Opacity
These controls change the opacity/transparency behavior of the particles. **Opacity** - the overall opacity multiplier. Values above one are acceptable and can make subtle particles more visible. **FadeInPower** - controls the falloff curve of the particle fade-in. **FadeOutPower** - controls the falloff curve of the particle fade-out. **SoftEdges** - enables the soft edges feature which fades out the particles where they intersect with scene geometry. **AlphaClipThreshold** - controls the opacity cut-off below which pixels are discarded and not drawn. The higher this value is, the more pixels can be discarded to reduce particle overdraw.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#scale)Scale
Controls the size of the particles. Particles transition from the ParticleStartSize to the ParticleEndSize over their lifetime. **ParticleStartSize** - the size of the particle (in meters) when it is born. **ParticleEndSize** - the size of the particle (in meters) when it dies.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#movement)Movement
These controls affect the movement of the particles. **ConstantFlow** - the smoothness of the flow of the particles. A value of 1 distributes particle flow evenly over time. A value of 0 spawns all of the particles and once right at the beginning of the phase. Values in between make particle birthrate/flow more random and hitchy. **ParticleSpeed** - controls the overall speed of the particles **ParticleDirection** - the main direction of particle movement **ParticleSpread** - the width of the particle emission cone in degrees. A value of 0 will emit particles in single direction and a value of 360 will emit particles in all directions (a sphere) **ParticleVelocityStart** - controls how fast the particles are moving when they’re first born. **ParticleVelocityEnd** - controls how fast the particles are moving when they die.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#rotation)Rotation
Controls the rotation behavior of the particles. **Rotation** - the static amount of rotation to apply to each particle in degrees. **RotationRandomOffset** - when checked, applies a random rotation amount to each particle **RotationSpeed** - the speed of rotation of each particle **RandomizeRotationDirection** - when true, each particle randomly either goes clockwise or counterclockwise.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#flipbook-1)Flipbook
Controls the behavior of the animated texture that is applied to the particles. **FlipbookTexture** - the flipbook texture to apply to the particles **FlipbookDimensions** - the number of rows and columns in the selected flipbook texture **FlipbookSpeed** - the playback frame rate of the flipbook. **MatchParticlePhase** - when true, the first frame of the flipbook will play when the particle is born and the last frame will play just before the particle dies - so the flipbook playback length will match the particle’s lifetime.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#forces)Forces
Control the external forces that affect the particle movement. **Gravity** - the pull of gravity on the particles. This is typically 0,-9.8, 0 - but some types of material, such as smoke or mist may be warm or lighter than air, which would cause them to move upward instead of getting pulled down by gravity. **Wind** - the direction and strength of the wind.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#debug)Debug
These controls allow you to debug specific parts of the particle system. **DebugTime** - When true, allows you to scrub time backwards and forward manually with the ManualTime slider. **ManualTime** - when DebugTime is true, you can use this slider to scrub time backwards and forward to see how the particles behave at different points during their lifetime.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#conditions)Conditions
This section illustrates two ways to branch your shader.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#branch-on-render-pipeline)Branch On Render Pipeline
Shader Graph allows you to create shaders that can be used in multiple render pipelines- Built-In, URP, and HDRP. This can be done by opening the shader in Shader Graph and adding the targets for all of the pipelines you want the shader to support in the Active Targets section under Graph Settings in the Graph Inspector window.
When supporting multiple render pipelines, it’s occasionally necessary to do different things in the graph depending on which pipeline is being used. In order to do that, you need to branch the shader based on the active render pipeline. There isn’t an official node in Shader Graph for performing that branching operation, but it is possible to create a subgraph that contains a Custom Function node that does the branch.
In this example, we use that Branch On RP to create a different outcome depending which render pipeline is active. In our simple example, we just make the cube a different color - green for URP, blue for HDRP, and yellow for the Built-In render pipeline - but you can do much more complex operations that are specific to each render pipeline using this same technique.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Feature-Examples.html#branch-on-material-quality)Branch On Material Quality
With Shader Graph, you can create one shader that has multiple different ways of achieving the same effect depending on how much GPU processing power you want to dedicate to it. This example illustrates that. We show three different methods of combining two normal maps together. The first method (at the top of the graph) is using the Normal Blend node set to Reoriented mode. This is the most accurate method that provides the best looking results, but it also requires the most compute power. The second method (in the middle of the graph) is almost as nice and a little bit cheaper. The third method (at the bottom of the graph) is the cheapest and produces the lowest quality result.
On the right side of the graph, you can see that the three different methods are connected to the Material Quality node. You can add a Material Quality node by opening the Blackboard and selecting Keyword->Material Quality from the add menu. Then drag the Material Quality parameter from the Blackboard into your graph. This node will select the top, middle, or bottom part of the graph depending on the Quality level that is selected.
In HDRP, the Quality setting is defined by the Default Material Quality Level setting found in the Material section of the HD Render Pipeline Asset. So for each Quality level, you define a pipeline asset, and that asset has the setting that controls which quality level the shader uses.
In a URP project, you can use the SetGlobalShaderKeywords command in the script that gets run when the user selects options in the application’s UI. For example, the following command will set Material Quality to High:
MaterialQualityUtilities.SetGlobalShaderKeywords( MaterialQuality.High );
Using the Material Quality node in Shader Graph enables you to provide the user with the ability to customize their experience in the application. They can choose to see higher quality visuals at a lower frame rate, or lower-quality visuals at a higher frame rate. And you control what these options do in the shader itself.


--- Page 55: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Terrain-Shaders.html ---

# Shaders
The names of these shaders indicate the [texture packing scheme](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Terrain-Packing.html) they use, the type of layers they’re using, and the technique used to blend the layers together.
You can either use these terrain shaders as provided in the sample, or keep them as reference to see how each layer works and then build your own terrain shader using the existing layer type nodes blended together with your choice of layer blend nodes.
Each of the example shaders uses four layers, but you can use fewer or more depending on the needs of your project. Just remember that each new layer makes the shader more expensive.
**CHNOS Array Dither** - this shader uses a technique that reduces texture samples as much as possible. The texture packing scheme packs the data from multiple materials into a single array texture. For each terrain material, the color and height data are stored in individual CH textures (color in RGB, height in the alpha channel). But the normal, occlusion, and smoothness for all of the materials on the terrain are packed into a single array texture. Because of this packing scheme, this 4-layer shader is able to do just 6 texture samples total, as opposed to the CNMSimpleBlend shader which requires 13. A dither pattern is used to blend out the hard edges that would otherwise appear when sampling an array texture.
**CHNOS Array Hex** - this shader uses the same packing scheme as the one above, but also includes hex grid tiling to break up texture repetition. This four-layer shader is doing just 15 texture samples, as opposed to the CNMHexHeight shader, which is doing 36. A dither pattern is used to blend out the hard edges that would otherwise appear when sampling an array texture.
**CNM BuiltIn Blend** - This shader is the most basic example of a terrain shader and matches the functionality of the existing terrain shader written in code. It uses the Built-In Terrain Layer nodes for each layer and uses the Blend2LayersBasic nodes to blend all of the layers together. It doesn’t do any tile break-up or fading between the near and far terrain materials. It is a good example of how the Terrain Layer Mask and Terrain Layer nodes can be used together to create a very simple and cheap terrain shader.
**CNM Hex Height** - This shader uses the LayerHex layer nodes (including one LayerHexDetail layer) - so it’s doing the hex tile method of repetition artifact break-up. It’s more expensive than the other shaders, but is the most effective at breaking up repetition. This shader also uses height blending for more realistic transitions between layers.
**CNM Rotation Height** - This shader uses LayerRot layer type - so it’s using the rotation method for tile break-up. It is not as effective as the hex tile method, but it’s cheaper. Layers are blended using height-based blending.
**CNM Simple Blend** - This shader is designed to be as simple as possible while still using a custom layer type - the LayerSimple type. It’s using simple lerp blending. In my testing this shader and CNMBiultInBlend performed the same - both of them very cheap.
**CNM Simple Height** - This shader is the same as CNMSimpleBlend, but it’s using height-based blending instead of lerp blending for a more realistic look.
**CNM Procedural Height** - This shader uses the Procedural method of breaking up the repetition. It’s similar to the Rotation method in that it samples the material textures twice, but the mask that blends between them is generated procedurally instead of using a mask texture. It’s more expensive than the Rotation method, but also more effective at tile break-up.
**CSNOH Auto Material Hex** - this example shader is similar to CSNOH Auto Material Simple, but it uses the hex grid tiling technique to break up the texture tiling.
**CSNOH Auto Material Rotation** - this example shader is similar to the one above, but it uses the rotation technique to break up texture tiling repetition.
**CSNOH Auto Material Simple** - this is an example of a shader that can be created to automatically apply materials to surfaces without requiring any manual painting or pre-generated splat maps. The shader uses the angle of the terrain along with the altitude to apply grass, dirt, rocks, cliff faces, and even snow in appropriate locations. At lower altitudes, the shader blends between grass on flat surfaces and dirt on more angled surfaces. At higher altitudes, the shader blends between rocky soil on flat surfaces and cliff faces on slopes. Then it blends the two together and adds snow on top.
**CSNOH Hex Blend** - This shader uses the Layer Hex CSNOH layer nodes - so it’s doing the hex tile method of repetition artifact break-up. It’s using standard alpha blending between the layers instead of height-based blending. It’s more expensive than CSNOH Simple Blend or CSNOH Rotation Height, but is the most effective at breaking up repetition.
**CSNOH Hex Height** - This shader uses the Layer Hex CSNOH layer nodes - so it’s doing the hex tile method of repetition artifact break-up. Layers are blended using height-based blending. It’s more expensive than CSNOH Simple Blend or CSNOH Rotation Height, but is the most effective at breaking up repetition.
**CSNOH Hex Parallax Height** - this shader is using both parallax mapping and hex grid tile break-up for every layer. It is extremely expensive because of the high number of texture samples required by all of the layers. We DO NOT recommend using a shader like this in production (where every layer is using the most expensive layer type). Instead, you should mix and match layer types based on the requirements of the materials you’re using. This example is included for performance and visual comparison purposes.
**CSNOH Parallax Height** - this shader uses parallax mapping - a form of ray marching, to create the illusion of tessellation and displacement on the surface of the terrain. Since we’re doing many texture samples, this technique can be quite expensive. Unlike this example which uses Layer Parallax CSNOH layers for every layer, we recommend using only one or two Layer Parallax CSNOH (for the materials that really need them) in your shaders to save on performance.
**CSNOH Rotation Height** - This shader uses Layer Rotation CSNOH layer type - so it’s using the rotation method for tile break-up. It is not as effective as the hex tile method, but it’s cheaper. Layers are blended using height-based blending.
**CSNOH Simple Blend** - This shader is designed to be as simple as possible while still using a custom layer type - the Layer Simple CSNOH type. It’s using simple alpha blending. In our testing this shader and CSNOH Simple Height performed the same - both of them very cheap (much cheaper than their CNM counterparts).
**CSNOH Simple Height** - This shader is the same as CSNOH Simple Blend, but it’s using height-based blending instead of lerp blending for a more realistic look.
**CSNOH Procedural Height** - This shader uses the Procedural method of breaking up the repetition. It’s similar to the Rotation method in that it samples the material textures twice, but the mask that blends between them is generated procedurally instead of using a mask texture. It’s more expensive than the Rotation method, but also more effective at tile break-up.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Sample-Terrain-Shaders.html#beyond-these-shaders)Beyond these shaders
While each of these sample shaders uses primarily one layer type and one type of blend node, you can mix and match them (and even create your own layer types and blend nodes) to get the specific features that you need for each individual layer. Maybe you have one layer with especially bad tiling artifacts. You could use the LayerHex layer type for that and then blend that into a Layer Triplanar layer that’s specifically for cliffs. The point is that you’re not locked into just one type of layer, so you can use some really cheap layers to save on performance and some fancier layers where you need more advanced features.


--- Page 56: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html ---

# Shader Graph Window
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html#description)Description
The **Shader Graph Window** contains the workspace for creating shaders with the **Shader Graph** system. To open the **Shader Graph Window** , you must first create a [Shader Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html). For more information, refer to the [Getting Started](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Getting-Started.html) section.
The **Shader Graph** window contains various individual elements such as the [Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackboard.html), [Graph Inspector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Internal-Inspector.html), and [Main Preview](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Main-Preview.html). You can move these elements around inside the workspace. They automatically anchor to the nearest corner when scaling the **Shader Graph Window**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html#toolbar)Toolbar
The toolbar at the top of the **Shader Graph Window** contains the following commands.
Icon | Item | Description  
---|---|---  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-save-icon.png) | **Save Asset** | Save the graph to update the [Shader Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html).  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-dropdown-icon.png) | **Save As** | Save the [Shader Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html) under a new name.  
| **Show In Project** | Highlight the [Shader Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html) in the [Project Window](https://docs.unity3d.com/Manual/ProjectView.html).  
| **Check Out** | If version control is enabled, check out the [Shader Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html) from the source control provider.  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-color-mode-selector.png) | **Color Mode Selector** | Select a [Color Mode](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Modes.html) for the graph.  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-blackboard-icon.png) | **Blackboard** | Toggle the visibility of the [Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackboard.html).  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-graph-inspector-icon.png) | **Graph Inspector** | Toggle the visibility of the [Graph Inspector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Internal-Inspector.html).  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-main-preview-icon.png) | **Main Preview** | Toggle the visibility of the [Main Preview](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Main-Preview.html).  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-help_icon.png) | **Help** | Open the Shader Graph documentation in the browser.  
![Image](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/images/sg-dropdown-icon.png) | **Resources** | Contains links to Shader Graph resources (like samples and User forums).  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html#workspace)Workspace
The workspace is where you create [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) networks. To navigate the workspace, do the following:
  * Press and hold the Alt key and drag with the left mouse button to pan.
  * Use the mouse scroll wheel to zoom in and out.


You can hold the left mouse button and drag to select multiple [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) with a marquee. There are also various [shortcut keys](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Keyboard-shortcuts.html) you can use for better workflow.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html#context-menu)Context Menu
Right-click within the workspace to open a context menu. However, if you right-click on an item within the workspace, such as a [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html), the context menu for that item opens. The workspace context menu provides the following options.
Item | Description  
---|---  
**Create Node** | Opens the [Create Node Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html).  
**Create Sticky Note** | Creates a new [Sticky Note](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sticky-Notes.html) on the Graph.  
**Collapse All Previews** | Collapses previews on all [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**Cut** | Removes the selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) from the graph and places them in the clipboard.  
**Copy** | Copies the selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) to the clipboard.  
**Paste** | Pastes the [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) from the clipboard.  
**Delete** | Deletes the selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**Duplicate** | Duplicates the selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**Select / Unused Nodes** | Selects all nodes on the graph that are not contributing to the final shader output from the [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Master-Stack.html).  
**View / Collapse Ports** | Collapses unused ports on all selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**View / Expand Ports** | Expands unused ports on all selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**View / Collapse Previews** | Collapses previews on all selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**View / Expand Previews** | Expands previews on all selected [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).  
**Precision / Inherit** | Sets the precision of all selected Nodes to Inherit.  
**Precision / Float** | Sets the precision of all selected nodes to Float.  
**Precision / Half** | Sets the precision of all selected nodes to Half.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html#additional-resources)Additional resources
  * [Color Modes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Modes.html)
  * [Create Node Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Create-Node-Menu.html)
  * [Keyboard shortcuts](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Keyboard-shortcuts.html)
  * [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Master-Stack.html)
  * [Nodes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html)
  * [Sticky Notes](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sticky-Notes.html)




--- Page 57: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Mapping-Node.html ---

# Parallax Mapping Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Mapping-Node.html#description)Description
The Parallax Mapping node lets you create a parallax effect that displaces a Material's UVs to create the illusion of depth inside a Material. This implementation uses the single step process that does not account for occlusion. For information on how the effect looks, see the [Height Map](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterHeightMap.html) page.
If you experience texture sampling errors while using this node in a graph which includes Custom Function Nodes or Sub Graphs, you can resolve them by upgrading to version 10.3 or later.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Mapping-Node.html#ports)Ports
Name | **Direction** | Type | Description  
---|---|---|---  
**Heightmap** | Input | Texture2D | The Texture that specifies the depth of the displacement.  
**Heightmap Sampler** | Input | Sampler State | The Sampler to sample **Heightmap** with.  
**Amplitude** | Input | Float | A multiplier to apply to the height of the Heightmap (in centimeters).  
**UVs** | Input | Vector2 | The UVs that the sampler uses to sample the Texture.  
**Parallax UVs** | Output | Vector2 | The UVs after adding the parallax offset.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Mapping-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 _ParallaxMapping_ParallaxUVs = UVs.xy + ParallaxMapping(Heightmap, Heightmap_Sampler, IN.TangentSpaceViewDirection, Amplitude * 0.01, UVs.xy);

```



--- Page 58: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html ---

# Slider Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html#description)Description
Defines a constant **Float** value in the shader using a **Slider** field. Can be converted to a **Float** type [Property](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html) with a **Mode** setting of **Slider** via the [Node's](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) context menu.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Slider |  | Defines the output value.  
Min | Float |  | Defines the slider parameter's minimum value.  
Max | Float |  | Defines the slider parameter's maximum value.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float _Slider_Out = 1.0;

```



--- Page 59: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Spherize-Node.html ---

# Spherize Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Spherize-Node.html#description)Description
Applies a spherical warping effect similar to a fisheye camera lens to the value of input **UV**. The center reference point of the warping effect is defined by input **Center** and the overall strength of the effect is defined by the value of input **Strength**. Input **Offset** can be used to offset the individual channels of the result.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Spherize-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Center | Input | Vector 2 | None | Center reference point  
Strength | Input | Float | None | Strength of the effect  
Offset | Input | Vector 2 | None | Individual channel offsets  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Spherize-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Spherize_float(float2 UV, float2 Center, float Strength, float2 Offset, out float2 Out)
{
    float2 delta = UV - Center;
    float delta2 = dot(delta.xy, delta.xy);
    float delta4 = delta2 * delta2;
    float2 delta_offset = delta4 * Strength;
    Out = UV + delta * delta_offset + Offset;
}

```



--- Page 60: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-bitmap-text-node.html ---

# Default Bitmap Text node
##### Note
Use this node only in shaders with **Material** set to **UI** for UI Toolkit. Using it elsewhere can lead to unexpected behavior or errors. For information on how to create shaders for UI Toolkit, refer to [UI Shader Graph](xref:uie-ui-shader-graph).
Outputs the text color set for bitmap text rendering and includes a tint input you can use to modify the color of the text. For example, if you connect a **Color** node to the tint input and set it to red, and connect the output to bitmap text render type, the text color of your bitmap text becomes red.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-bitmap-text-node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Tint | Input | Color | The color tint to apply to the text.  
Bitmap text | Output | Texture | The rendered bitmap of the text.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-bitmap-text-node.html#additional-resources)Additional resources
  * [Default Solid node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html)
  * [Default Gradient node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html)
  * [Default Texture node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html)
  * [Default SDF Text node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html)
  * [Render Type Branch node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/render-type-branch-node.html)




--- Page 61: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html ---

# Default Solid node
##### Note
Use this node only in shaders with **Material** set to **UI** for UI Toolkit. Using it elsewhere can lead to unexpected behavior or errors. For information on how to create shaders for UI Toolkit, refer to [UI Shader Graph](xref:uie-ui-shader-graph).
Outputs the solid color specified for your UI elements, such as the background color of a button. For example, if you set the background color of a button to yellow, the **Default Solid** node outputs yellow for that button.
You can use this node combined with other nodes to create custom effects for the Solid color render type. For example, you can multiply the output of this node with a **Color** node to filter unwanted colors.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Solid | Output | Color | The solid color specified for the UI element.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html#additional-resources)Additional resources
  * [Default Gradient node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html)
  * [Default Texture node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html)
  * [Default SDF Text node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html)
  * [Default Bitmap Text node](xref:default-bitmap-text-node)
  * [Render Type Branch node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/render-type-branch-node.html)




--- Page 62: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html ---

# Subgraph Asset
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html#description)Description
The **Subgraph Asset** is a new **Asset** type introduced with the Shader Graph. A **Subgraph Asset** defines a [Subgraph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html). This is different to a Shader Graph. You can create a **Subgraph Asset** from the [Project window](https://docs.unity3d.com/Manual/ProjectView.html.md) from the **Create** menu via **Subgraph** in the **Shader** sub-menu.
You can open the [Shader Graph Window](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Graph-Window.html) by double clicking a **Subgraph Asset** or by clicking **Open Shader Editor** in the [Inspector](https://docs.unity3d.com/Manual/UsingTheInspector.html) when the **Subgraph Asset** is selected.


--- Page 63: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html ---

# Sub Graph
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html#description)Description
A Sub Graph is a special type of Shader Graph, which you can reference from inside other graphs. This is useful when you wish to perform the same operations multiple times in one graph or across multiple graphs. A Sub Graph differs from a Shader Graph in three main ways:
  * [Properties](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Property-Types.html) in the [Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackboard.html) of a Sub Graph define the input [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) of a [Sub Graph Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html) when you reference the Sub Graph from inside another graph.
  * A Sub Graph has its own Asset type. For more information, including instructions on how to make a new Sub Graph, see [Sub Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html).
  * A Sub Graph does not have a [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Master-Stack.html). Instead, it has a [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) called **Output**.


For information about the components of a Sub Graph, see [Sub Graph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html#output-node)Output Node
The Output Node defines the output ports of a [Sub Graph Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html) when you reference the Sub Graph from inside another graph. To add and remove ports, use the [Custom Port Menu](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Port-Menu.html) in the **Node Settings** tab of the [Graph Inspector](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Internal-Inspector.html) by clicking on the Sub Graph Output node.
The preview used for Sub Graphs is determined by the first port of the Output Node. Valid [Data Types](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) for the first port are `Float`, `Vector 2`, `Vector 3`, `Vector 4`, `Matrix2`, `Matrix3`, `Matrix4`, and `Boolean`. Any other data type will produce an error in the preview shader and the Sub Graph will become invalid.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html#sub-graphs-and-shader-stages)Sub Graphs and shader stages
If a Node within a Sub Graph specifies a shader stage (for example, how the [Sample Texture 2D Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Node.html) specifies the **fragment** shader stage), the Editor locks the entire Sub Graph to that stage. You cannot connect any Nodes that specify a different shader stage to the Sub Graph Output Node, and the Editor locks any Sub Graph Nodes that references the graph to that shader stage.
From 10.3 onward, Texture and SamplerState type inputs and outputs to Sub Graphs benefit from an improved data structure. For a detailed explanation, see [Custom Function Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Function-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html#sub-graphs-and-keywords)Sub Graphs and Keywords
[Keywords](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Keywords.html) that you define on the [Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackboard.html) in a Sub Graph behave similarly to those in regular Shader Graphs. When you add a Sub Graph Node to a Shader Graph, Unity defines all Keywords in that Sub Graph in the Shader Graph as well, so that the Sub Graph works as intended.
To use a Sub Graph Keyword inside a Shader Graph, or to expose that Keyword in the Material Inspector, copy it from the Sub Graph to the Shader Graph's Blackboard.


--- Page 64: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html ---

# Default SDF Text node
##### Note
Use this node only in shaders with **Material** set to **UI** for UI Toolkit. Using it elsewhere can lead to unexpected behavior or errors. For information on how to create shaders for UI Toolkit, refer to [UI Shader Graph](xref:uie-ui-shader-graph).
Outputs the text color for SDF text rendering and includes a tint input you can use to modify the color of the text. For example, if you connect a **Color** node to the tint input and set it to red, and connect the output to SDF text render type, the text color of your SDF text becomes red.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Tint | Input | Color | The tint color to apply to the text.  
SDF Text | Output | Texture | The rendered SDF text as a texture.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html#additional-resources)Additional resources
  * [Default Solid node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html)
  * [Default Gradient node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html)
  * [Default Texture node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html)
  * [Default Bitmap Text node](xref:default-bitmap-text-node)
  * [Render Type Branch node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/render-type-branch-node.html)




--- Page 65: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html ---

# Voronoi Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html#description)Description
Generates a Voronoi, or [Worley](https://en.wikipedia.org/wiki/Worley_noise), noise based on input **UV**. Voronoi noise is generated by calculating distances between a pixel and a lattice of points. By offsetting these points by a pseudo-random number, controlled by input **Angle Offset** , a cluster of cells can be generated. The scale of these cells, and the resulting noise, is controlled by input **Cell Density**. The output **Cells** contains the raw cell data.
You can also choose to use two different hashing methods for calculating the noise. As of Unity version 2021.2, the Voronoi node defaults to the **Deterministic** hash, to ensure consistent results for noise generation across platforms.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Angle Offset | Input | Float | None | Offset value for points  
Cell Density | Input | Float | None | Density of cells generated  
Out | Output | Float | None | Output noise value  
Cells | Output | Float | None | Raw cell data  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Hash Type | Dropdown | Deterministic, LegacySine | Selects the hash function used to generate random numbers for noise generation.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
inline float2 unity_voronoi_noise_randomVector (float2 UV, float offset)
{
    float2x2 m = float2x2(15.27, 47.63, 99.41, 89.98);
    UV = frac(sin(mul(UV, m)) * 46839.32);
    return float2(sin(UV.y*+offset)*0.5+0.5, cos(UV.x*offset)*0.5+0.5);
}

void Unity_Voronoi_float(float2 UV, float AngleOffset, float CellDensity, out float Out, out float Cells)
{
    float2 g = floor(UV * CellDensity);
    float2 f = frac(UV * CellDensity);
    float3 res = float3(8.0, 0.0, 0.0);

    for(int y=-1; y<=1; y++)
    {
        for(int x=-1; x<=1; x++)
        {
            float2 lattice = float2(x,y);
            float2 offset = unity_voronoi_noise_randomVector(lattice + g, AngleOffset);
            float d = distance(lattice + offset, f);
            if(d < res.x)
            {
                res = float3(d, offset.x, offset.y);
                Out = res.x;
                Cells = res.y;
            }
        }
    }
}

```



--- Page 66: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html ---

# Triplanar Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html#description)Description
Generates UVs and samples a texture by projecting in world space. This method is commonly used to texture large models such as terrain, where hand authoring UV coordinates would either be problematic or not performant. Samples the input **Texture** 3 times, once in each of the world x, y, and z axes. The resulting information is planar projected onto the model, blended by the normal, or surface angle. You can scale the generated UVs with the input **Tile** and you can control the final blending strength with the input **Blend**.
**Blend** controls the way the normal affects the blending of each plane sample and should be greater than or equal to 0. The larger **Blend** is, the more contribution will be given to the sample from the plane towards which the normal is most oriented. (The maximum blend exponent is between 17 and 158 depending on the platform and the precision of the node.) A **Blend** of 0 makes each plane get equal weight regardless of normal orientation.
To choose the projection, change the **Input Space**. You can also modify the projection via the inputs **Position** and **Normal**.
Use the **Type** dropdown to change the expected type of the input **Texture**. If set to **Normal** , the **Out** port returns the blended normals in **Normal Output Space**.
If you experience texture sampling errors while using this node in a graph which includes Custom Function Nodes or Sub Graphs, upgrade to version 10.3 or later.
NOTE: You can only use the Triplanar Node in the **Fragment** shader stage.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Texture | Input | Texture | None | Input texture value  
Sampler | Input | Sampler State | None | Sampler for input **Texture**  
Position | Input | Vector 3 | Input Space Position | Fragment position  
Normal | Input | Vector 3 | Input Space Normal | Fragment normal  
Tile | Input | Float | None | Tiling amount for generated UVs  
Blend | Input | Float | None | Blend factor between different samples  
Out | Output | Vector 4 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Type | Dropdown | Default, Normal | Type of input **Texture**  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html#node-settings-controls)Node Settings Controls
The following controls appear on the Node Settings tab of the Graph Inspector, when you select the Triplanar Node.
Name | Type | Options | Description  
---|---|---|---  
Input Space | Dropdown | Object, View, World, Tangent, AbsoluteWorld | Controls the coordinate space used by the input ports **Position** and **Normal**. When you change the **Input Space** value, it changes the bindings on the **Position** and **Normal** ports to use the specified space. The default value is **AbsoluteWorld**.  
Normal Output Space | Dropdown | Object, View, World, Tangent, AbsoluteWorld | Controls the coordinate space used for the **Out** port. The Normal Output Space control is only available when **Type** is set to **Normal**. The default value is **Tangent**.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
**Default**
```
float3 Node_UV = Position * Tile;
float3 Node_Blend = pow(abs(Normal), Blend);
Node_Blend /= dot(Node_Blend, 1.0);
float4 Node_X = SAMPLE_TEXTURE2D(Texture, Sampler, Node_UV.zy);
float4 Node_Y = SAMPLE_TEXTURE2D(Texture, Sampler, Node_UV.xz);
float4 Node_Z = SAMPLE_TEXTURE2D(Texture, Sampler, Node_UV.xy);
float4 Out = Node_X * Node_Blend.x + Node_Y * Node_Blend.y + Node_Z * Node_Blend.z;

```

**Normal**
```
float3 Node_UV = Position * Tile;
float3 Node_Blend = max(pow(abs(Normal), Blend), 0);
Node_Blend /= (Node_Blend.x + Node_Blend.y + Node_Blend.z ).xxx;
float3 Node_X = UnpackNormal(SAMPLE_TEXTURE2D(Texture, Sampler, Node_UV.zy));
float3 Node_Y = UnpackNormal(SAMPLE_TEXTURE2D(Texture, Sampler, Node_UV.xz));
float3 Node_Z = UnpackNormal(SAMPLE_TEXTURE2D(Texture, Sampler, Node_UV.xy));
Node_X = float3(Node_X.xy + Normal.zy, abs(Node_X.z) * Normal.x);
Node_Y = float3(Node_Y.xy + Normal.xz, abs(Node_Y.z) * Normal.y);
Node_Z = float3(Node_Z.xy + Normal.xy, abs(Node_Z.z) * Normal.z);
float4 Out = float4(normalize(Node_X.zyx * Node_Blend.x + Node_Y.xzy * Node_Blend.y + Node_Z.xyz * Node_Blend.z), 1);
float3x3 Node_Transform = float3x3(IN.WorldSpaceTangent, IN.WorldSpaceBiTangent, IN.WorldSpaceNormal);
Out.rgb = TransformWorldToTangent(Out.rgb, Node_Transform);

```



--- Page 67: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html ---

# Default Texture node
##### Note
Use this node only in shaders with **Material** set to **UI** for UI Toolkit. Using it elsewhere can lead to unexpected behavior or errors. For information on how to create shaders for UI Toolkit, refer to [UI Shader Graph](xref:uie-ui-shader-graph).
Provides the texture assigned to the UI element.
You can use this node to access the texture assigned to a UI element, such as a Texture 2D background image. The node includes UV and tint inputs that allow you to modify how the texture is applied. For example, you can connect a **Tiling and Offset** node to the UV input to create a repeating effect for the background image, or connect a **Color** node to the tint input to adjust the tint color of the background image.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
UV | Input | Vector2 | The UV coordinates for the texture.  
Tint | Input | Color | The tint color to apply to the texture.  
Texture | Output | Texture | The resulting texture.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html#additional-resources)Additional resources
  * [Default Solid node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html)
  * [Default Gradient node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html)
  * [Default SDF Text node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html)
  * [Default Bitmap Text node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-bitmap-text-node.html)




--- Page 68: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html ---

# Split Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html#description)Description
Splits the input vector **In** into four **Float** outputs **R** , **G** , **B** and **A**. These output vectors are defined by the individual channels of the input **In** ; red, green, blue and alpha respectively. If the input vector **In** 's dimension is less than 4 (**Vector 4**) the output values not present in the input will be 0.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
R | Output | Float | None | Red channel from input  
G | Output | Float | None | Green channel from input  
B | Output | Float | None | Blue channel from input  
A | Output | Float | None | Alpha channel from input  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float _Split_R = In[0];
float _Split_G = In[1];
float _Split_B = 0;
float _Split_A = 0;

```



--- Page 69: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html ---

# Default Gradient node
##### Note
Use this node only in shaders with **Material** set to **UI** for UI Toolkit. Using it elsewhere can lead to unexpected behavior or errors. For information on how to create shaders for UI Toolkit, refer to [UI Shader Graph](xref:uie-ui-shader-graph).
Outputs the gradient specified for your UI elements. For example, if you set the background image of a button to use a vector graphic with a linear gradient from top red to bottom green, the Default Gradient node outputs that gradient for the button.
You can use the Default Gradient node combined with other nodes to create custom effects for the gradient render type. For example, you can multiply the output of this node with a **Color** node to filter unwanted colors from the gradient.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Gradient | Output | Gradient | The gradient specified for the UI element.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-gradient-node.html#additional-resources)Additional resources
  * [Default Solid node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-solid-node.html)
  * [Default Texture node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-texture-node.html)
  * [Default SDF Text node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/default-sdf-text-node.html)
  * [Default Bitmap Text node](xref:default-bitmap-text-node)
  * [Render Type Branch node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/render-type-branch-node.html)




--- Page 70: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html ---

# Swizzle Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html#description)Description
Creates a new [vector](https://docs.unity3d.com/Manual/VectorCookbook.html) from the reordered elements of the input vector. This is called swizzling.
To specify how input elements should be swizzled, enter a formatting string in the input mask. To invert the order of the input elements, for example, use the string "wzyx" or "abgr".
The length of the input mask determines the dimensions of the output vector. The error "Invalid Mask" indicates an input mask value which includes one or more channels that do not exist in the input vector.
To output a vector3 with the x, y and z elements of the input vector, for example, use the input mask “xyz” or “rgb”.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Dynamic Vector | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Mask | Inputfield | x, y, z, w (depending on input vector dimension) | The swizzle mask is a combination of one to four characters that can be x, y, z, w (or r, g, b, a). The size of output value depends on the length of the mask input.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float4 _Swizzle_Out = In.wzyx;

```



--- Page 71: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html ---

# Subgraph node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html#description)Description
Provides a reference to a [Subgraph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html). All ports on the reference node are defined by the properties and outputs defined in the Subgraph Asset. This is useful for sharing functionality between graphs or duplicating the same functionality within a graph.
The preview used for a Subgraph Node is determined by the first port of that [Subgraph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html) Output node. Valid [Data Types](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) for the first port are `Float`, `Vector 2`, `Vector 3`, `Vector 4`, `Matrix2`, `Matrix3`, `Matrix4`, and `Boolean`. Any other data type will produce an error in the preview shader and the Subgraph will become invalid.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html#subgraph-nodes-and-shader-stages)Subgraph Nodes and Shader Stages
If a [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) within a Subgraph specifies a [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html), such as how [Sample Texture 2D Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Node.html) specifies the **fragment** Shader Stage, then that entire Subgraph) is now locked to that stage. As such a Subgraph node that references the graph will also be locked to that Shader Stage.
Furthermore, when an [Edge](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) connected to an output [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) on a **Subgraph Node** flows into a port on the [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Master-Stack.html) that **Subgraph Node** is now locked to the Shader Stage of that [Block Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html) in the Master Stack.

