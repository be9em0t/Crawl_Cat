
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


--- Page 3: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html ---

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


--- Page 4: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Math-Nodes.html ---

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


--- Page 6: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Input-Nodes.html ---

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


--- Page 7: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html ---

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


--- Page 9: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Render-Texture-Nodes.html ---

# Custom Render Texture nodes
Access properties and data of custom render textures, including size, slice index, cubemap face, and previous update state.
**Topic** | **Description**  
---|---  
[Custom Render Texture Slice](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Slice.html) | Access the custom render texture slice index and cubemap face.  
[Custom Render Texture Size](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Size.html) | Access the custom render texture size.  
[Custom Render Texture Self](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Custom-Texture-Self.html) | Access the custom render texture from the previous update.


--- Page 10: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Nodes.html ---

# Channel nodes
Combine, split, reorder, or flip vector and color channels.
**Topic** | **Description**  
---|---  
[Append](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html) | Combine two float or vector inputs into a single new vector of variable dimensions.  
[Combine](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html) | Creates new vectors from the four inputs R, G, B and A.  
[Flip](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html) | Flips the individual channels of input In selected by the node's parameters.  
[Split](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html) | Splits the input vector In into four Float outputs R, G, B and A.  
[Swizzle](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html) | Creates a new vector from the reordered elements of the input vector.


--- Page 11: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Nodes.html ---

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


--- Page 12: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Absolute-Node.html ---

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



--- Page 13: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Boolean-Node.html ---

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



--- Page 14: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Node.html ---

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



--- Page 15: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mask-Node.html ---

# Channel Mask Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mask-Node.html#description)Description
Masks values of input **In** on channels selected in dropdown **Channels**. Outputs a vector of the same length as the input vector but with the selected channels set to 0. Channels available in the dropdown **Channels** will represent the amount of channels present in input **In**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mask-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Dynamic Vector | None | Input value  
Out | Output | Dynamic Vector | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mask-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Channels | Mask Dropdown | Dynamic | Selects any number of channels to mask  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mask-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_ChannelMask_RedGreen_float4(float4 In, out float4 Out)
{
    Out = float4(0, 0, In.b, In.a);
}

```



--- Page 16: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html ---

# Branch node
The Branch node adds a dynamic branch to the shader, which outputs a different value depending on whether the input is true or false.
Both sides of the branch are evaluated in the shader, and the output from the unused path is discarded.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**Predicate** | Input | Boolean | None | The input to test the value of. If you input a float, all values are evaluated as `true` except `0`.  
**True** | Input | Dynamic Vector | None | The value to output as **Out** if **Predicate** is true.  
**False** | Input | Dynamic Vector | None | The value to output as **Out** if **Predicate** is false.  
**Out** | Output | Dynamic Vector | None | Outputs either **True** or **False**.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Branch_float4(float Predicate, float4 True, float4 False, out float4 Out)
{
    Out = Predicate ? True : False;
}

```



--- Page 17: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Camera-Node.html ---

# Camera Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Camera-Node.html#description)Description
Provides access to various parameters of the **Camera** currently being used for rendering. This is comprised of values the **Camera** 's GameObject, such as Position and Direction, as well as various projection parameters.
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Camera-Node.html#unity-render-pipelines-support)Unity Render Pipelines Support
  * Universal Render Pipeline


The High Definition Render Pipeline does **not** support this Node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Camera-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Position | Output | Vector 3 | None | Position of the Camera's GameObject in world space  
Direction | Output | Vector 3 | None | The Camera's forward vector direction  
Orthographic | Output | Float | None | Returns 1 if the Camera is orthographic, otherwise 0  
Near Plane | Output | Float | None | The Camera's near plane distance  
Far Plane | Output | Float | None | The Camera's far plane distance  
Z Buffer Sign | Output | Float | None | Returns -1 when using a reversed Z Buffer, otherwise 1  
Width | Output | Float | None | The Camera's width if orthographic  
Height | Output | Float | None | The Camera's height if orthographic  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Camera-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float3 _Camera_Position = _WorldSpaceCameraPos;
float3 _Camera_Direction = -UNITY_MATRIX_V[2].xyz;
float _Camera_Orthographic = unity_OrthoParams.w;
float _Camera_NearPlane = _ProjectionParams.y;
float _Camera_FarPlane = _ProjectionParams.z;
float _Camera_ZBufferSign = _ProjectionParams.x;
float _Camera_Width = unity_OrthoParams.x;
float _Camera_Height = unity_OrthoParams.y;

```



--- Page 18: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Checkerboard-Node.html ---

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



--- Page 19: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blend-Node.html ---

# Blend Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blend-Node.html#description)Description
Blends the value of input **Blend** onto input **Base** using the blending mode defined by the **Mode** parameter. The strength of the blend is defined by input **Opacity**. An **Opacity** value of 0 will return the input **Base** , unaltered.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blend-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Base | Input | Dynamic Vector | None | Base layer value  
Blend | Input | Dynamic Vector | None | Blend layer value  
Opacity | Input | Float | None | Strength of blend  
Out | Output | Dynamic Vector | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blend-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Mode | Dropdown | Burn, Darken, Difference, Dodge, Divide, Exclusion, HardLight, HardMix, Lighten, LinearBurn, LinearDodge, LinearLight, LinearLightAddSub, Multiply, Negation, Overlay, PinLight, Screen, SoftLight, Subtract, VividLight, Overwrite | Blend mode to apply  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blend-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per blend mode.
**Burn**
```
void Unity_Blend_Burn_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out =  1.0 - (1.0 - Blend)/Base;
    Out = lerp(Base, Out, Opacity);
}

```

**Darken**
```
void Unity_Blend_Darken_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = min(Blend, Base);
    Out = lerp(Base, Out, Opacity);
}

```

**Difference**
```
void Unity_Blend_Difference_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = abs(Blend - Base);
    Out = lerp(Base, Out, Opacity);
}

```

**Dodge**
```
void Unity_Blend_Dodge_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Base / (1.0 - Blend);
    Out = lerp(Base, Out, Opacity);
}

```

**Divide**
```
void Unity_Blend_Divide_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Base / (Blend + 0.000000000001);
    Out = lerp(Base, Out, Opacity);
}

```

**Exclusion**
```
void Unity_Blend_Exclusion_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Blend + Base - (2.0 * Blend * Base);
    Out = lerp(Base, Out, Opacity);
}

```

**HardLight**
```
void Unity_Blend_HardLight_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    float4 result1 = 1.0 - 2.0 * (1.0 - Base) * (1.0 - Blend);
    float4 result2 = 2.0 * Base * Blend;
    float4 zeroOrOne = step(Blend, 0.5);
    Out = result2 * zeroOrOne + (1 - zeroOrOne) * result1;
    Out = lerp(Base, Out, Opacity);
}

```

**HardMix**
```
void Unity_Blend_HardMix_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = step(1 - Base, Blend);
    Out = lerp(Base, Out, Opacity);
}

```

**Lighten**
```
void Unity_Blend_Lighten_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = max(Blend, Base);
    Out = lerp(Base, Out, Opacity);
}

```

**LinearBurn**
```
void Unity_Blend_LinearBurn_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Base + Blend - 1.0;
    Out = lerp(Base, Out, Opacity);
}

```

**LinearDodge**
```
void Unity_Blend_LinearDodge_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Base + Blend;
    Out = lerp(Base, Out, Opacity);
}

```

**LinearLight**
```
void Unity_Blend_LinearLight_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Blend < 0.5 ? max(Base + (2 * Blend) - 1, 0) : min(Base + 2 * (Blend - 0.5), 1);
    Out = lerp(Base, Out, Opacity);
}

```

**LinearLightAddSub**
```
void Unity_Blend_LinearLightAddSub_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Blend + 2.0 * Base - 1.0;
    Out = lerp(Base, Out, Opacity);
}

```

**Multiply**
```
void Unity_Blend_Multiply_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Base * Blend;
    Out = lerp(Base, Out, Opacity);
}

```

**Negation**
```
void Unity_Blend_Negation_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = 1.0 - abs(1.0 - Blend - Base);
    Out = lerp(Base, Out, Opacity);
}

```

**Overlay**
```
void Unity_Blend_Overlay_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    float4 result1 = 1.0 - 2.0 * (1.0 - Base) * (1.0 - Blend);
    float4 result2 = 2.0 * Base * Blend;
    float4 zeroOrOne = step(Base, 0.5);
    Out = result2 * zeroOrOne + (1 - zeroOrOne) * result1;
    Out = lerp(Base, Out, Opacity);
}

```

**PinLight**
```
void Unity_Blend_PinLight_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    float4 check = step (0.5, Blend);
    float4 result1 = check * max(2.0 * (Base - 0.5), Blend);
    Out = result1 + (1.0 - check) * min(2.0 * Base, Blend);
    Out = lerp(Base, Out, Opacity);
}

```

**Screen**
```
void Unity_Blend_Screen_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = 1.0 - (1.0 - Blend) * (1.0 - Base);
    Out = lerp(Base, Out, Opacity);
}

```

**SoftLight**
```
void Unity_Blend_SoftLight_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    float4 result1 = 2.0 * Base * Blend + Base * Base * (1.0 - 2.0 * Blend);
    float4 result2 = sqrt(Base) * (2.0 * Blend - 1.0) + 2.0 * Base * (1.0 - Blend);
    float4 zeroOrOne = step(0.5, Blend);
    Out = result2 * zeroOrOne + (1 - zeroOrOne) * result1;
    Out = lerp(Base, Out, Opacity);
}

```

**Subtract**
```
void Unity_Blend_Subtract_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = Base - Blend;
    Out = lerp(Base, Out, Opacity);
}

```

**VividLight**
```
void Unity_Blend_VividLight_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    float4 result1 = 1.0 - (1.0 - Blend) / (2.0 * Base);
    float4 result2 = Blend / (2.0 * (1.0 - Base));
    float4 zeroOrOne = step(0.5, Base);
    Out = result2 * zeroOrOne + (1 - zeroOrOne) * result1;
    Out = lerp(Base, Out, Opacity);
}

```

**Overwrite**
```
void Unity_Blend_Overwrite_float4(float4 Base, float4 Blend, float Opacity, out float4 Out)
{
    Out = lerp(Base, Blend, Opacity);
}

```



--- Page 20: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Mask-Node.html ---

# Color Mask Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Mask-Node.html#description)Description
Creates a mask from values in input **In** equal to input **Mask Color**. Input **Range** can be used to define a wider range of values around input **Mask Color** to create the mask. Colors within this range will return 1, otherwise the node will return 0. Input **Fuzziness** can be used to soften the edges around the selection similar to anti-aliasing.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Mask-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value.  
Mask Color | Input | Vector 3 | Color | Color to use for mask.  
Range | Input | Float | None | Select colors within this range from input **Mask Color**.  
Fuzziness | Input | Float | None | Feather edges around selection. Higher values result in a softer selection mask.  
Out | Output | Float | None | Output mask value.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Color-Mask-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_ColorMask_float(float3 In, float3 MaskColor, float Range, float Fuzziness, out float4 Out)
{
    float Distance = distance(MaskColor, In);
    Out = saturate(1 - (Distance - Range) / max(Fuzziness, 1e-5));
}

```



--- Page 21: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html ---

# Baked GI Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html#description)Description
Provides access to the **Baked GI** values at the vertex or fragment's position. Requires **Position** and **Normal** input for light probe sampling, and lightmap coordinates **Static UV** and **Dynamic UV** for all potential lightmap sampling cases.
Note: The behavior of this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined globally. Shader Graph does not define the function of the node. Instead, each Render Pipeline defines what HLSL code to execute for this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
Different Render Pipelines may produce different results. If you're building a shader in one Render Pipeline that you want to use in both, try checking it in both pipelines before production. A [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) might be defined in one Render Pipeline and undefined in the other. If this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined, it returns 0 (black).
###  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html#unity-render-pipelines-support)Unity Render Pipelines Support
This node is compatible with both the High Definition Render Pipeline (HDRP) and the Universal Render Pipeline (URP). However, this node does not work within unlit shaders for either pipeline.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Position | Input | Vector 3 | Position (world space) | Mesh vertex/fragment's **Position**  
Normal | Input | Vector 3 | Normal (world space) | Mesh vertex/fragment's **Normal**  
Static UV | Input | Vector 2 | UV1 | Lightmap coordinates for the static lightmap  
Dynamic UV | Input | Vector 2 | UV2 | Lightmap coordinates for the dynamic lightmap  
Out | Output | Vector 3 | None | Output color value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Apply Lightmap Scaling | Toggle | True, False | If enabled lightmaps are automatically scaled and offset.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Baked-GI-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_BakedGI_float(float3 Position, float3 Normal, float2 StaticUV, float2 DynamicUV, out float Out)
{
    Out = SHADERGRAPH_BAKED_GI(Position, Normal, StaticUV, DynamicUV, false);
}

```



--- Page 22: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Bitangent-Vector-Node.html ---

# Bitangent Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Bitangent-Vector-Node.html#description)Description
Provides access to the mesh vertex or fragment's **Bitangent Vector** , depending on the effective [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html) of the graph section the [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is part of.
The bitangent vector is derived from the normal and tangent vectors and is orthogonal to both. The three vectors provide a reference frame to perform complex light calculations, for example.
You can select the coordinate space of the output with the **Space** dropdown parameter.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Bitangent-Vector-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 3 | None |  **Bitangent Vector** for the Mesh Vertex/Fragment.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Bitangent-Vector-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Space | Dropdown | Object, View, World, Tangent | Selects coordinate space of **Bitangent Vector** to output.


--- Page 23: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/And-Node.html ---

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



--- Page 24: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ceiling-Node.html ---

# Ceiling Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ceiling-Node.html#description)Description
Returns the smallest integer value, or whole number, that is greater than or equal to the value of input **In**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ceiling-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ceiling-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Ceiling_float4(float4 In, out float4 Out)
{
    Out = ceil(In);
}

```



--- Page 25: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackbody-Node.html ---

# Blackbody Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackbody-Node.html#description)Description
Samples a **Gradient** that simulates the effect of black body radiation. The calculations in this node are based on data gathered by Mitchell Charity. This node outputs color in linear RGB space and preforms the conversion using a D65 whitepoint and a CIE 1964 10 degree color space. For more information, see [What color is a blackbody?](http://www.vendian.org/mncharity/dir3/blackbody/)
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackbody-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Temperature | Input | Float | None | Temperature or temperature map in Kelvin to sample.  
Out | Output | Vector 3 | None | Intensity represented by color in Vector 3.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Blackbody-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Blackbody_float(float Temperature, out float3 Out)
{
    float3 color = float3(255.0, 255.0, 255.0);
    color.x = 56100000. * pow(Temperature,(-3.0 / 2.0)) + 148.0;
    color.y = 100.04 * log(Temperature) - 623.6;
    if (Temperature > 6500.0) color.y = 35200000.0 * pow(Temperature,(-3.0 / 2.0)) + 184.0;
    color.z = 194.18 * log(Temperature) - 1448.6;
    color = clamp(color, 0.0, 255.0)/255.0;
    if (Temperature < 1000.0) color *= Temperature/1000.0;
    Out = color;
}

```



--- Page 26: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Channel-Mixer-Node.html ---

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



--- Page 27: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ambient-Node.html ---

# Ambient Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ambient-Node.html#description)Description
Provides access to the Scene's **Ambient** color values. When Environment Lighting Source is set to **Gradient** [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **Color/Sky** returns the value **Sky Color**. When Environment Lighting Source is set to **Color** [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **Color/Sky** returns the value **Ambient Color**. [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **Equator** and **Ground** always return the values **Equator Color** and **Ground Color** regardless of the current Environment Lighting Source.
Note: Values of this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) are only updated when entering Play mode or saving the current Scene/Project.
Note: The behavior of this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined globally. Shader Graph does not define the function of the node. Instead, each Render Pipeline defines what HLSL code to execute for this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
Different Render Pipelines may produce different results. If you're building a shader in one Render Pipeline that you want to use in both, try checking it in both pipelines before production. A [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) might be defined in one Render Pipeline and undefined in the other. If this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined, it returns 0 (black).
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ambient-Node.html#unity-render-pipelines-support)Unity Render Pipelines Support
  * Universal Render Pipeline


The High Definition Render Pipeline does **not** support this Node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ambient-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Color/Sky | Output | Vector 3 | None | Color (Color) or Sky (Gradient) color value  
Equator | Output | Vector 3 | None | Equator (Gradient) color value  
Ground | Output | Vector 3 | None | Ground (Gradient) color value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ambient-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float3 _Ambient_ColorSky = SHADERGRAPH_AMBIENT_SKY;
float3 _Ambient_Equator = SHADERGRAPH_AMBIENT_EQUATOR;
float3 _Ambient_Ground = SHADERGRAPH_AMBIENT_GROUND;

```



--- Page 28: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Any-Node.html ---

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



--- Page 29: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/All-Node.html ---

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



--- Page 30: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Clamp-Node.html ---

# Clamp Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Clamp-Node.html#description)Description
Returns the input **In** clamped between the minimum and maximum values defined by inputs **Min** and **Max** respectively.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Clamp-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Unclamped input value  
Min | Input | Dynamic Vector | Minimum value  
Max | Input | Dynamic Vector | Maximum value  
Out | Output | Dynamic Vector | Clamped output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Clamp-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Clamp_float4(float4 In, float4 Min, float4 Max, out float4 Out)
{
    Out = clamp(In, Min, Max);
}

```



--- Page 31: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Add-Node.html ---

# Add Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Add-Node.html#description)Description
Returns the sum of the two input values **A** and **B**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Add-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Add-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Add_float4(float4 A, float4 B, out float4 Out)
{
    Out = A + B;
}

```



--- Page 32: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Append-Node.html ---

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



--- Page 33: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html ---

# Colorspace Conversion Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html#description)Description
Returns the result of converting the value of input **In** from one colorspace space to another. The spaces to transform from and to are defined by the values of the dropdowns on the node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Vector 3 | Input value  
Out | Output | Vector 3 | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
From | Dropdown | RGB, Linear, HSV | Selects the colorspace to convert from  
To | Dropdown | RGB, Linear, HSV | Selects the colorspace to convert to  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Colorspace-Conversion-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per from/to permutation.
**RGB > RGB**
```
void Unity_ColorspaceConversion_RGB_RGB_float(float3 In, out float3 Out)
{
    Out =  In;
}

```

**RGB > Linear**
```
void Unity_ColorspaceConversion_RGB_Linear_float(float3 In, out float3 Out)
{
    float3 linearRGBLo = In / 12.92;;
    float3 linearRGBHi = pow(max(abs((In + 0.055) / 1.055), 1.192092896e-07), float3(2.4, 2.4, 2.4));
    Out = float3(In <= 0.04045) ? linearRGBLo : linearRGBHi;
}

```

**RGB > HSV**
```
void Unity_ColorspaceConversion_RGB_HSV_float(float3 In, out float3 Out)
{
    float4 K = float4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    float4 P = lerp(float4(In.bg, K.wz), float4(In.gb, K.xy), step(In.b, In.g));
    float4 Q = lerp(float4(P.xyw, In.r), float4(In.r, P.yzx), step(P.x, In.r));
    float D = Q.x - min(Q.w, Q.y);
    float  E = 1e-10;
    Out = float3(abs(Q.z + (Q.w - Q.y)/(6.0 * D + E)), D / (Q.x + E), Q.x);
}

```

**Linear > RGB**
```
void Unity_ColorspaceConversion_Linear_RGB_float(float3 In, out float3 Out)
{
    float3 sRGBLo = In * 12.92;
    float3 sRGBHi = (pow(max(abs(In), 1.192092896e-07), float3(1.0 / 2.4, 1.0 / 2.4, 1.0 / 2.4)) * 1.055) - 0.055;
    Out = float3(In <= 0.0031308) ? sRGBLo : sRGBHi;
}

```

**Linear > Linear**
```
void Unity_ColorspaceConversion_Linear_Linear_float(float3 In, out float3 Out)
{
    Out = In;
}

```

**Linear > HSV**
```
void Unity_ColorspaceConversion_Linear_HSV_float(float3 In, out float3 Out)
{
    float3 sRGBLo = In * 12.92;
    float3 sRGBHi = (pow(max(abs(In), 1.192092896e-07), float3(1.0 / 2.4, 1.0 / 2.4, 1.0 / 2.4)) * 1.055) - 0.055;
    float3 Linear = float3(In <= 0.0031308) ? sRGBLo : sRGBHi;
    float4 K = float4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    float4 P = lerp(float4(Linear.bg, K.wz), float4(Linear.gb, K.xy), step(Linear.b, Linear.g));
    float4 Q = lerp(float4(P.xyw, Linear.r), float4(Linear.r, P.yzx), step(P.x, Linear.r));
    float D = Q.x - min(Q.w, Q.y);
    float  E = 1e-10;
    Out = float3(abs(Q.z + (Q.w - Q.y)/(6.0 * D + E)), D / (Q.x + E), Q.x);
}

```

**HSV > RGB**
```
void Unity_ColorspaceConversion_HSV_RGB_float(float3 In, out float3 Out)
{
    float4 K = float4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    float3 P = abs(frac(In.xxx + K.xyz) * 6.0 - K.www);
    Out = In.z * lerp(K.xxx, saturate(P - K.xxx), In.y);
}

```

**HSV > Linear**
```
void Unity_ColorspaceConversion_HSV_Linear_float(float3 In, out float3 Out)
{
    float4 K = float4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    float3 P = abs(frac(In.xxx + K.xyz) * 6.0 - K.www);
    float3 RGB = In.z * lerp(K.xxx, saturate(P - K.xxx), In.y);
    float3 linearRGBLo = RGB / 12.92;
    float3 linearRGBHi = pow(max(abs((RGB + 0.055) / 1.055), 1.192092896e-07), float3(2.4, 2.4, 2.4));
    Out = float3(RGB <= 0.04045) ? linearRGBLo : linearRGBHi;
}

```

**HSV > HSV**
```
void Unity_ColorspaceConversion_HSV_HSV_float(float3 In, out float3 Out)
{
    Out = In;
}

```



--- Page 34: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Exponential-Node.html ---

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



--- Page 35: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Divide-Node.html ---

# Divide Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Divide-Node.html#description)Description
Returns the result of input **A** (dividend) divided by input **B** (divisor).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Divide-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Divide-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Divide_float4(float4 A, float4 B, out float4 Out)
{
    Out = A / B;
}

```



--- Page 36: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html ---

# Fraction Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html#description)Description
Returns the fractional (or decimal) part of input **In** ; which is greater than or equal to 0 and less than 1.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Fraction_float4(float4 In, out float4 Out)
{
    Out = frac(In);
}

```



--- Page 37: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDY-Node.html ---

# DDY Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDY-Node.html#description)Description
Returns the partial derivative of the input **In** with respect to the screen-space y-coordinate. This node can only be used in the pixel shader stage.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDY-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output partial derivative value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDY-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_DDY_float4(float4 In, out float4 Out)
{
    Out = ddy(In);
}

```



--- Page 38: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Floor-Node.html ---

# Floor Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Floor-Node.html#description)Description
Returns the largest integer value, or whole number, that is less than or equal to the value of input **In**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Floor-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Floor-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Floor_float4(float4 In, out float4 Out)
{
    Out = floor(In);
}

```



--- Page 39: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Contrast-Node.html ---

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



--- Page 40: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dither-Node.html ---

# Dither node
The Dither node adds a structured form of noise to the input. Use the Dither node to reduce the color bands that might appear if you move from a high number of colors to a low number (quantizing), or to simulate transparency by adding random alpha pixels to an opaque object.
The Dither node applies dithering in screen space to ensure a uniform distribution of the pattern. To change the space the node uses, connect another node to the **Screen Position** input, such as a [UV node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Nodes.html).
To use a dither pattern for transparency, connect the Dither node to the **Alpha Clip Threshold** input in the [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Master-Stack.html). As a result, when you adjust the overall alpha value of the material, some pixels are discarded because the alpha value is lower than their alpha clip threshold. This technique is useful for creating geometry that appears to be transparent but has the advantages of rendering as opaque, such as writing to the depth buffer or rendering using a deferred [rendering path](https://docs.unity3d.com/Manual/built-in-rendering-paths.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dither-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**In** | Input | Dynamic vector | None | The input to dither. The noise stays within the overall minimum and maximum range of the input values.  
**Screen Position** | Input | Vector 4 | Screen Position | The coordinates Unity uses to calculate the dither pattern. For more information about the options, refer to the [Screen Position node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html).  
**Out** | Output | Dynamic vector | None | The dithered output.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dither-Node.html#generated-code-example)Generated code example
The following example code represents one possible outcome of this node.
```
void Unity_Dither_float4(float4 In, float4 ScreenPosition, out float4 Out)
{
    float2 uv = ScreenPosition.xy * _ScreenParams.xy;
    float DITHER_THRESHOLDS[16] =
    {
        1.0 / 17.0,  9.0 / 17.0,  3.0 / 17.0, 11.0 / 17.0,
        13.0 / 17.0,  5.0 / 17.0, 15.0 / 17.0,  7.0 / 17.0,
        4.0 / 17.0, 12.0 / 17.0,  2.0 / 17.0, 10.0 / 17.0,
        16.0 / 17.0,  8.0 / 17.0, 14.0 / 17.0,  6.0 / 17.0
    };
    uint index = (uint(uv.x) % 4) * 4 + uint(uv.y) % 4;
    Out = In - DITHER_THRESHOLDS[index];
}

```



--- Page 41: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fog-Node.html ---

# Fog Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fog-Node.html#description)Description
Provides access to the Scene's **Fog** parameters.
Note: The behavior of this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined globally. Shader Graph does not define the function of the node. Instead, each Render Pipeline defines what HLSL code to execute for this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
Different Render Pipelines may produce different results. If you're building a shader in one Render Pipeline that you want to use in both, try checking it in both pipelines before production. A [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) might be defined in one Render Pipeline and undefined in the other. If this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined, it returns 0 (black).
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fog-Node.html#unity-render-pipelines-support)Unity Render Pipelines Support
  * Universal Render Pipeline


The High Definition Render Pipeline does **not** support this Node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fog-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Position | Input | Vector 3 | Position (object space) | Mesh vertex/fragment's position  
Color | Output | Vector 4 | None | Fog color  
Density | Output | Float | None | Fog density based on depth. Returns a value between 0 and 1, where 0 is no fog and 1 is full fog.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fog-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Fog_float(float3 Position, out float4 Color, out float Density)
{
    SHADERGRAPH_FOG(Position, Color, Density);
}

```



--- Page 42: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flipbook-Node.html ---

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



--- Page 43: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDX-Node.html ---

# DDX Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDX-Node.html#description)Description
Returns the partial derivative of the input **In** with respect to the screen-space x-coordinate. This node can only be used in the pixel shader stage.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDX-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output partial derivative value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDX-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_DDX_float4(float4 In, out float4 Out)
{
    Out = ddx(In);
}

```



--- Page 44: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Ellipse-Node.html ---

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



--- Page 45: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Constant-Node.html ---

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



--- Page 46: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Flip-Node.html ---

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



--- Page 47: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Compute-Deformation-Node.html ---

# Compute Deformation Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Compute-Deformation-Node.html#description)Description
This node lets you pass compute deformed vertex data to a vertex shader, and only works with the [Entities Graphics package](https://docs.unity3d.com/Packages/com.unity.entities.graphics@latest/). You must provide `DeformedVertexData` in the `_DeformedMeshData` buffer. The node uses the `_ComputeMeshIndex` property to calculate where the `DeformedVertexData` associated with the current mesh are located in the `_DeformedMeshData` buffer. To output data, you must either install both the Entities Graphics package and DOTS Animation packages, or use a custom solution.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Compute-Deformation-Node.html#ports)Ports
Name | Direction | Type | Stage | Description  
---|---|---|---|---  
Position | Output | Vector3 | Vertex | Outputs the deformed vertex position.  
Normal | Output | Vector3 | Vertex | Outputs the deformed vertex normal.  
Tangent | Output | Vector3 | Vertex | Outputs the deformed vertex tangent.


--- Page 48: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Combine-Node.html ---

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



--- Page 49: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDXY-Node.html ---

# DDXY Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDXY-Node.html#description)Description
Returns the sum of both partial derivatives of input **In** , with respect to the screen-space x-coordinate and screen-space y-coordinate respectively. This node can only be used in the pixel shader stage.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDXY-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output partial derivative value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/DDXY-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_DDXY_float4(float4 In, out float4 Out)
{
    Out = ddxy(In);
}

```



--- Page 50: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Float-Node.html ---

# Float Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Float-Node.html#description)Description
Defines a **Float** value in the shader. If [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **X** is not connected with an [Edge](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) defines a constant **Float**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Float-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
X | Input | Float | None | Input x component value  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Float-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float _Vector1_Out = X;

```



--- Page 51: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dielectric-Specular-Node.html ---

# Dielectric Specular Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dielectric-Specular-Node.html#description)Description
Returns a **Dielectric Specular** F0 value for a physically based material. The material to use can be selected with the **Material** dropdown parameter on the [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
A **Common** **Material** type defines a range between 0.034 and 0.048 sRGB values. The value between this range can be selected with the **Range** parameter. This **Material** type should be used for various materials such as plastics and fabrics.
You can use **Custom** material type to define your own physically based material value. The output value in this case is defined by its index of refraction. This can be set by the parameter **IOR**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dielectric-Specular-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dielectric-Specular-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Material | Dropdown | Common, RustedMetal, Water, Ice, Glass, Custom | Selects the material value to output.  
Range | Slider |  | Controls output value for **Common** material type.  
IOR | Slider |  | Controls index of refraction for **Custom** material type.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Dielectric-Specular-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Material** mode.
**Common**
```
float _DielectricSpecular_Range = 0.5;
float _DielectricSpecular_Out = lerp(0.034, 0.048, _DielectricSpecular_Range);

```

**RustedMetal**
```
float _DielectricSpecular_Out = 0.030;

```

**Water**
```
float _DielectricSpecular_Out = 0.020;

```

**Ice**
```
float _DielectricSpecular_Out = 0.018;

```

**Glass**
```
float _DielectricSpecular_Out = 0.040;

```

**Custom**
```
float _DielectricSpecular_IOR = 1;
float _DielectricSpecular_Out = pow(_Node_IOR - 1, 2) / pow(_DielectricSpecular_IOR + 1, 2);

```



--- Page 52: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Comparison-Node.html ---

# Comparison Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Comparison-Node.html#description)Description
Compares the two input values **A** and **B** based on the condition selected on the dropdown. This is often used as an input to the [Branch Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Comparison-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
A | Input | Float | None | First input value  
B | Input | Float | None | Second input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Comparison-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Dropdown | Equal, NotEqual, Less, LessOrEqual, Greater, GreaterOrEqual | Condition for comparison  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Comparison-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per comparison type.
**Equal**
```
void Unity_Comparison_Equal_float(float A, float B, out float Out)
{
    Out = A == B ? 1 : 0;
}

```

**NotEqual**
```
void Unity_Comparison_NotEqual_float(float A, float B, out float Out)
{
    Out = A != B ? 1 : 0;
}

```

**Less**
```
void Unity_Comparison_Less_float(float A, float B, out float Out)
{
    Out = A < B ? 1 : 0;
}

```

**LessOrEqual**
```
void Unity_Comparison_LessOrEqual_float(float A, float B, out float Out)
{
    Out = A <= B ? 1 : 0;
}

```

**Greater**
```
void Unity_Comparison_Greater_float(float A, float B, out float Out)
{
    Out = A > B ? 1 : 0;
}

```

**GreaterOrEqual**
```
void Unity_Comparison_GreaterOrEqual_float(float A, float B, out float Out)
{
    Out = A >= B ? 1 : 0;
}

```



--- Page 53: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Noise-Node.html ---

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



--- Page 54: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Hue-Node.html ---

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



--- Page 55: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Node.html ---

# Gradient Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Node.html#description)Description
Defines a constant **Gradient** for use in [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/index.html), although internally to the shader this is defined as a **struct**. To sample the **Gradient** it should be used in conjunction with a [Sample Gradient Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Gradient-Node.html). When using a separate **Gradient Node** , you can sample a **Gradient** multiple times with different Time parameters.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Out | Output | Gradient | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Gradient Field |  | Defines the gradient.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Gradient-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
Gradient Unity_Gradient_float()
{
    Gradient g;
    g.type = 1;
    g.colorsLength = 4;
    g.alphasLength = 4;
    g.colors[0] = 0.1;
    g.colors[1] = 0.2;
    g.colors[2] = 0.3;
    g.colors[3] = 0.4;
    g.colors[4] = 0;
    g.colors[5] = 0;
    g.colors[6] = 0;
    g.colors[7] = 0;
    g.alphas[0] = 0.1;
    g.alphas[1] = 0.2;
    g.alphas[2] = 0.3;
    g.alphas[3] = 0.4;
    g.alphas[4] = 0;
    g.alphas[5] = 0;
    g.alphas[6] = 0;
    g.alphas[7] = 0;
    return g;
}

Gradient _Gradient = Unity_Gradient_float();

```



--- Page 56: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-Infinite-Node.html ---

# Is Infinite Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-Infinite-Node.html#description)Description
Returns true if the input **In** is an infinite value. This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-Infinite-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Float | None | Input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-Infinite-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_IsInfinite_float(float In, out float Out)
{
    Out = isinf(In);
}

```



--- Page 57: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Linear-Blend-Skinning-Node.html ---

# Linear Blend Skinning Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Linear-Blend-Skinning-Node.html#description)Description
This node lets you apply Linear Blend Vertex Skinning, and only works with the [Entities Graphics package](https://docs.unity3d.com/Packages/com.unity.entities.graphics@latest/). You must provide skinned matrices in the `_SkinMatrices` buffer. The node uses the `_SkinMatrixIndex` property to calculate where the matrices associated with the current mesh are located in the `_SkinMatrices` buffer.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Linear-Blend-Skinning-Node.html#ports)Ports
Name | Direction | Type | Stage | Description  
---|---|---|---|---  
Position | Input | Vector3 | Vertex | Position of the vertex in object space.  
Normal | Input | Vector3 | Vertex | Normal of the vertex in object space.  
Tangent | Input | Vector3 | Vertex | Tangent of the vertex in object space.  
Position | Output | Vector3 | Vertex | Outputs the skinned vertex position.  
Normal | Output | Vector3 | Vertex | Outputs the skinned vertex normal.  
Tangent | Output | Vector3 | Vertex | Outputs the skinned vertex tangent.


--- Page 58: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html ---

# Matrix Split Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html#description)Description
Splits a square matrix defined by input **In** into vectors. Output vector dimension is defined by the dimension of the input matrix.
The dropdown on the node can be used to select whether the output values are taken from the rows or columns of the input matrix.
  * **Row** : Output vectors are composed of matrix rows from top to bottom.
  * **Column** : Output vectors are composed of matrix columns from left to right.


An input matrix of type **Matrix 2x2** or **Matrix 3x3** will return 0 values in the rows (or columns, depending on dropdown selection) that are beyond their dimension.
For example, connecting **Matrix 2x2** type to input **In** will return the correct **Vector 2** type outputs to output slots **M0** and **M1** , leaving outputs **M2** and **M3** to return 0 values.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Matrix | Input value  
M0 | Output | Dynamic Vector | First row or column  
M1 | Output | Dynamic Vector | Second row or column  
M2 | Output | Dynamic Vector | Third row or column  
M3 | Output | Dynamic Vector | Fourth row or column  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Dropdown | Row, Column | Selects how the output vectors should be filled  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Split-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 _MatrixSplit_M0 = float2(In[0].r, In[0].g);
float2 _MatrixSplit_M1 = float2(In[1].r, In[1].g);
float2 _MatrixSplit_M2 = float2(0, 0);
float2 _MatrixSplit_M3 = float2(0, 0);

```



--- Page 59: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Maximum-Node.html ---

# Maximum Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Maximum-Node.html#description)Description
Returns the largest of the two inputs values **A** and **B**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Maximum-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Maximum-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Maximum_float4(float4 A, float4 B, out float4 Out)
{
    Out = max(A, B);
}

```



--- Page 60: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Integer-Node.html ---

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



--- Page 61: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-2x2-Node.html ---

# Matrix 2x2 Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-2x2-Node.html#description)Description
Defines a constant **Matrix 2x2** value in the shader.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-2x2-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Matrix 2 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-2x2-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Matrix 2x2 |  | Sets output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-2x2-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2x2 _Matrix2x2 = float2x2(1, 0, 0, 1);

```



--- Page 62: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Log-Node.html ---

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

```

**Base 2**
```
void Unity_Log2_float4(float4 In, out float4 Out)
{
    Out = log2(In);
}

```

**Base 10**
```
void Unity_Log10_float4(float4 In, out float4 Out)
{
    Out = log10(In);
}

```



--- Page 63: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Determinant-Node.html ---

# Matrix Determinant
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Determinant-Node.html#description)Description
Returns the determinant of the matrix defined by input **In**. It can be viewed as the scaling factor of the transformation described by the matrix.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Determinant-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Matrix | Input value  
Out | Output | Float | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Determinant-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_MatrixDeterminant_float4x4(float4x4 In, out float Out)
{
    Out = determinant(In);
}

```



--- Page 64: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-3x3-Node.html ---

# Matrix 3x3 Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-3x3-Node.html#description)Description
Defines a constant **Matrix 3x3** value in the shader.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-3x3-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Matrix 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-3x3-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Matrix 3x3 |  | Sets output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-3x3-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float3x3 _Matrix3x3 = float3x3(1, 0, 0, 0, 1, 0, 0, 0, 1);

```



--- Page 65: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Inverse-Lerp-Node.html ---

# Inverse Lerp Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Inverse-Lerp-Node.html#description)Description
Returns the linear parameter that produces the interpolant specified by input **T** within the range of input **A** to input **B**.
**Inverse Lerp** is the inverse operation of the [Lerp Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html). It can be used to determine what the input to a [Lerp](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html) was based on its output.
For example, the value of a **Lerp** between 0 and 2 with a **T** value of 0.5 is 1. Therefore the value of an **Inverse Lerp** between 0 and 2 with a **T** value of 1 is 0.5.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Inverse-Lerp-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
T | Input | Dynamic Vector | Time value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Inverse-Lerp-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_InverseLerp_float4(float4 A, float4 B, float4 T, out float4 Out)
{
    Out = (T - A)/(B - A);
}

```



--- Page 66: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html ---

# Lerp Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html#description)Description
Returns the result of linearly interpolating between input **A** and input **B** by input **T**.
The output is calculated as `A + T * (B - A)`. The value of input **T** acts as a weight factor applied to the difference between **B** and **A** :
  * When **T** is `0`, the output equals **A**.
  * When **T** is `1`, the output equals **B**.
  * When **T** is `0.5`, the output is the midpoint between **A** and **B**.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
T | Input | Dynamic Vector | Time value. Typical range: 0 to 1. Though you can use values outside of this range they may cause unpredictable results.  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Lerp_float4(float4 A, float4 B, float4 T, out float4 Out)
{
    Out = lerp(A, B, T);
}

```



--- Page 67: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Invert-Colors-Node.html ---

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



--- Page 68: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Construction-Node.html ---

# Matrix Construction Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Construction-Node.html#description)Description
Constructs square matrices from the four input vectors **M0** , **M1** , **M2** and **M3**. This node can be used to generate matrices of types **Matrix 2x2** , **Matrix 3x3** and **Matrix 4x4**.
The dropdown on the node can be used to select whether the inputs values specify the matrix rows or columns.
  * **Row** : Input vectors specify matrix rows from top to bottom.
  * **Column** : Input vectors specify matrix columns from left to right.


Matrix outputs are taken from the top left corner of the construction of the inputs. This can be used to generate different dimension square matrices from different dimension vectors.
For example, connecting **Vector 2** type values to inputs **M0** and **M1** will generate the desired matrix from the output **2x2**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Construction-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
M0 | Input | Vector 4 | First row or column  
M1 | Input | Vector 4 | Second row or column  
M2 | Input | Vector 4 | Third row or column  
M3 | Input | Vector 4 | Fourth row or column  
4x4 | Output | Matrix 4x4 | Output as Matrix 4x4  
3x3 | Output | Matrix 3x3 | Output as Matrix 3x3  
2x2 | Output | Matrix 2x2 | Output as Matrix 2x2  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Construction-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Dropdown | Row, Column | Selects how the output matrix should be filled  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Construction-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per mode.
**Row**
```
void Unity_MatrixConstruction_Row_float(float4 M0, float4 M1, float4 M2, float3 M3, out float4x4 Out4x4, out float3x3 Out3x3, out float2x2 Out2x2)
{
    Out4x4 = float4x4(M0.x, M0.y, M0.z, M0.w, M1.x, M1.y, M1.z, M1.w, M2.x, M2.y, M2.z, M2.w, M3.x, M3.y, M3.z, M3.w);
    Out3x3 = float3x3(M0.x, M0.y, M0.z, M1.x, M1.y, M1.z, M2.x, M2.y, M2.z);
    Out2x2 = float2x2(M0.x, M0.y, M1.x, M1.y);
}

```

**Column**
```
void Unity_MatrixConstruction_Column_float(float4 M0, float4 M1, float4 M2, float3 M3, out float4x4 Out4x4, out float3x3 Out3x3, out float2x2 Out2x2)
{
    Out4x4 = float4x4(M0.x, M1.x, M2.x, M3.x, M0.y, M1.y, M2.y, M3.y, M0.z, M1.z, M2.z, M3.z, M0.w, M1.w, M2.w, M3.w);
    Out3x3 = float3x3(M0.x, M1.x, M2.x, M0.y, M1.y, M2.y, M0.z, M1.z, M2.z);
    Out2x2 = float2x2(M0.x, M1.x, M0.y, M1.y);
}

```



--- Page 69: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-4x4-Node.html ---

# Matrix 4x4 Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-4x4-Node.html#description)Description
Defines a constant **Matrix 4x4** value in the shader.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-4x4-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Matrix 4 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-4x4-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Matrix 4x4 |  | Sets output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-4x4-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float4x4 _Matrix4x4 = float4x4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);

```



--- Page 70: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Transpose-Node.html ---

# Matrix Transpose
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Transpose-Node.html#description)Description
Returns the transposed value of the matrix defined by input **In**. This can be seen as the operation of flipping the matrix over its diagonal. The result is that it switches the row and column indices of the matrix.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Transpose-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Matrix | Input value  
Out | Output | Dynamic Matrix | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Matrix-Transpose-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_MatrixTranspose_float4x4(float4x4 In, out float4x4 Out)
{
    Out = transpose(In);
}

```



--- Page 71: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-NaN-Node.html ---

# Is NaN Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-NaN-Node.html#description)Description
Returns true if the input **In** is not a number (NaN). This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-NaN-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Float | None | Input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Is-NaN-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_IsNan_float(float In, out float Out)
{
    Out = (In < 0.0 || In > 0.0 || In == 0.0) ? 0 : 1;
}

```



--- Page 72: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Length-Node.html ---

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

```



--- Page 73: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Minimum-Node.html ---

# Minimum Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Minimum-Node.html#description)Description
Returns the smallest of the two inputs values **A** and **B**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Minimum-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Minimum-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Minimum_float4(float4 A, float4 B, out float4 Out)
{
    Out = min(A, B);
}

```



--- Page 74: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Modulo-Node.html ---

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



--- Page 75: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Multiply-Node.html ---

# Multiply Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Multiply-Node.html#description)Description
Returns the result of input **A** multiplied by input **B**. If both inputs are a vector type, the output type will be a vector type with the same dimension as the evaluated type of those inputs. If both inputs are a matrix type, the output type will be a matrix type with the same dimension as the evaluated type of those inputs. If one input is a vector type and the other is a matrix type, then output type will be a vector with the same dimension as the vector type input.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Multiply-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic | First input value  
B | Input | Dynamic | Second input value  
Out | Output | Dynamic | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Multiply-Node.html#generated-code-example)Generated Code Example
The following example code represents different possible outcomes of this node.
**Vector * Vector**
```
void Unity_Multiply_float4_float4(float4 A, float4 B, out float4 Out)
{
    Out = A * B;
}

```

**Vector * Matrix**
```
void Unity_Multiply_float4_float4x4(float4 A, float4x4 B, out float4 Out)
{
    Out = mul(A, B);
}

```

**Matrix * Matrix**
```
void Unity_Multiply_float4x4_float4x4(float4x4 A, float4x4 B, out float4x4 Out)
{
    Out = mul(A, B);
}

```



--- Page 76: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Not-Node.html ---

# Not node
The Not node outputs the opposite of an input. If the input is true the output is false, otherwise the output is true. This node is useful for [branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Not-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**In** | Input | Boolean | None | The input value.  
**Out** | Output | Boolean | None | The opposite of **In**.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Not-Node.html#generated-code-example)Generated code example
The following example code represents one possible outcome of this node.
```
Out = !In;

```



--- Page 77: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Metal-Reflectance-Node.html ---

# Metal Reflectance Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Metal-Reflectance-Node.html#description)Description
Returns a **Metal Reflectance** value for a physically based material. The material to use can be selected with the **Material** dropdown parameter on the [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
When using **Specular** **Workflow** on a [PBR Master Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/PBR-Master-Node.md) this value should be supplied to the **Specular** [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html). When using **Metallic** **Workflow** this value should be supplied to the **Albedo** [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Metal-Reflectance-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Metal-Reflectance-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Material | Dropdown | Iron, Silver, Aluminium, Gold, Copper, Chromium, Nickel, Titanium, Cobalt, Platform | Selects the material value to output.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Metal-Reflectance-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
**Iron**
```
float3 _MetalReflectance_Out = float3(0.560, 0.570, 0.580);

```

**Silver**
```
float3 _MetalReflectance_Out = float3(0.972, 0.960, 0.915);

```

**Aluminium**
```
float3 _MetalReflectance_Out = float3(0.913, 0.921, 0.925);

```

**Gold**
```
float3 _MetalReflectance_Out = float3(1.000, 0.766, 0.336);

```

**Copper**
```
float3 _MetalReflectance_Out = float3(0.955, 0.637, 0.538);

```

**Chromium**
```
float3 _MetalReflectance_Out = float3(0.550, 0.556, 0.554);

```

**Nickel**
```
float3 _MetalReflectance_Out = float3(0.660, 0.609, 0.526);

```

**Titanium**
```
float3 _MetalReflectance_Out = float3(0.542, 0.497, 0.449);

```

**Cobalt**
```
float3 _MetalReflectance_Out = float3(0.662, 0.655, 0.634);

```

**Platinum**
```
float3 _MetalReflectance_Out = float3(0.672, 0.637, 0.585);

```



--- Page 78: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/One-Minus-Node.html ---

# One Minus Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/One-Minus-Node.html#description)Description
Returns the result of input **In** subtracted from 1.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/One-Minus-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/One-Minus-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_OneMinus_float4(float4 In, out float4 Out)
{
    Out = 1 - In;
}

```



--- Page 79: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Negate-Node.html ---

# Negate Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Negate-Node.html#description)Description
Returns the flipped sign value of input **In**. Positive values become negative and negative values become positive.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Negate-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Negate-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Negate_float4(float4 In, out float4 Out)
{
    Out = -1 * In;
}

```



--- Page 80: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Vector-Node.html ---

# Normal Vector node
The Normal Vector node outputs the normal of a vertex or fragment of a mesh.
For more information about normals, refer to [Normal maps](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterNormalMapLanding.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Vector-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**Out** | Output | Vector 3 | None | The normal of the vertex or fragment of the mesh, depending on the [shader stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html) of the graph section.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Vector-Node.html#space)Space
The **Space** dropdown determines the coordinate space of the normal vector.
**Option** | **Description**  
---|---  
**Object** | Returns the vertex or fragment normal in object space, where up is the up axis of local space.  
**View** | Returns the vertex or fragment normal in view space, where up is the up direction of the camera.  
**World** | Returns the vertex or fragment normal in world space, where up is the up direction of the scene.  
**Tangent** | Returns the vertex or fragment normal in tangent space, where up is away from the surface of the mesh.


--- Page 81: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Strength-Node.html ---

# Normal Strength Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Strength-Node.html#description)Description
Adjusts the strength of the normal map defined by input **In** by the amount of input **Strength**. A **Strength** value of 1 will return the input unaltered. A **Strength** value of 0 will return a blank normal map.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Strength-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value  
Strength | Input | Float | None | Strength value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Strength-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_NormalStrength_float(float3 In, float Strength, out float3 Out)
{
    Out = {precision}3(In.rg * Strength, lerp(1, In.b, saturate(Strength)));
}

```



--- Page 82: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normalize-Node.html ---

# Normalize Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normalize-Node.html#description)Description
Returns the normalized value of input **In**. The output vector will have the same direction as input **In** but a length of 1.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normalize-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normalize-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Normalize_float4(float4 In, out float4 Out)
{
    Out = normalize(In);
}

```



--- Page 83: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Object-Node.html ---

# Object node
The Object node outputs the position, scale, or bounds of the overall GameObject that Unity is currently rendering.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Object-Node.html#render-pipeline-compatibility)Render pipeline compatibility
The Object node is compatible with the following render pipelines:
  * Universal Render Pipeline (URP)
  * High Definition Render Pipeline (HDRP)


**Note:** The output of the **Position** port might depend on the render pipeline you use. If you use your shader in both URP and HDRP, check the results in both pipelines before you use the shader in production.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Object-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**Position** | Output | Vector 3 | None | The position of the overall GameObject in world space.  
**Scale** | Output | Vector 3 | None | The scale of the overall GameObject in world space  
**World Bounds Min** | Output | Vector 3 | None | The minimum position of the axis-aligned bounding box that fully encloses the GameObject in world space.  
**World Bounds Max** | Output | Vector 3 | None | The maximum position of the bounding box.  
**Bounds Size** | Output | Vector 3 | None | The total size of the bounding box.  
**Note:** The bounds values are equivalent to the [bounds in the Renderer component](https://docs.unity3d.com/ScriptReference/Renderer-bounds.html) of the GameObject. If you deform the vertices in the shader graph, the bounds in the Renderer component don't change.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Object-Node.html#generated-code-example)Generated code example
The following example code represents one possible outcome of this node.
```
float3 _Object_Position = SHADERGRAPH_OBJECT_POSITION;
float3 _Object_Scale = float3(length(float3(UNITY_MATRIX_M[0].x, UNITY_MATRIX_M[1].x, UNITY_MATRIX_M[2].x)),
                             length(float3(UNITY_MATRIX_M[0].y, UNITY_MATRIX_M[1].y, UNITY_MATRIX_M[2].y)),
                             length(float3(UNITY_MATRIX_M[0].z, UNITY_MATRIX_M[1].z, UNITY_MATRIX_M[2].z)));
float3 _Object_WorldBoundsMin = SHADERGRAPH_RENDERER_BOUNDS_MIN;
float3 _Object_WorldBoundsMax = SHADERGRAPH_RENDERER_BOUNDS_MAX;
float3 _Object_BoundsSize = (SHADERGRAPH_RENDERER_BOUNDS_MAX - SHADERGRAPH_RENDERER_BOUNDS_MIN);

```



--- Page 84: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Nand-Node.html ---

# Nand Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Nand-Node.html#description)Description
Returns true if both the inputs **A** and **B** are false. This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Nand-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
A | Input | Boolean | None | First input value  
B | Input | Boolean | None | Second input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Nand-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Nand_float(float A, float B, out float Out)
{
    Out = !A && !B;
}

```



--- Page 85: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Unpack-Node.html ---

# Normal Unpack Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Unpack-Node.html#description)Description
Unpacks a normal map defined by input **In**. This node is used to unpack a texture that is defined as a **Normal Map** in its Texture Import Settings when it is sampled as if it were a default texture.
Data is stored in textures from 0 to 1. But vectors need to be from -1 to 1. Unpacking the normal means to expand its range from the original range to a range of -1 to 1, so you can use it as a vector.
Note that in most cases this node is unnecessary as the normal map should be sampled as such by setting its **Type** parameter to **Normal** when it is sampled using a [Sample Texture 2D](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Node.html) or [Triplanar](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html) node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Unpack-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 4 | None | Input value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Unpack-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Space | Dropdown | Tangent, Object | Sets the coordinate space of the input normal.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Unpack-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Space** mode.
**Tangent**
```
void Unity_NormalUnpack_float(float4 In, out float3 Out)
{
    Out = UnpackNormalMapRGorAG(In);
}

```

**Object**
```
void Unity_NormalUnpackRGB_float(float4 In, out float3 Out)
{
    Out = UnpackNormalmapRGB(In);
}

```



--- Page 86: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Or-Node.html ---

# Or Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Or-Node.html#description)Description
Returns true if either of the inputs **A** and **B** are true. This is useful for [Branching](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Branch-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Or-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
A | Input | Boolean | None | First input value  
B | Input | Boolean | None | Second input value  
Out | Output | Boolean | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Or-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Or_float(float In, out float Out)
{
    Out = A || B;
}

```



--- Page 87: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Blend-Node.html ---

# Normal Blend Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Blend-Node.html#description)Description
Blends two normal maps defined by inputs **A** and **B** , normalizing the result to produce a valid normal map representing the combined surface detail.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Blend-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
A | Input | Vector 3 | None | First input normal map  
B | Input | Vector 3 | None | Second input normal map  
Out | Output | Vector 3 | None | Blended normal map  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Blend-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Mode | Dropdown | Default | Blends the two normal maps by adding their x and y components and multiplying their z components, then normalizes the result to ensure a valid normal direction.  
Mode | Dropdown | Reoriented | Blends the two normal maps using a mathematically correct method, ensuring the resulting normal map represents a realistic combined surface.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-Blend-Node.html#generated-code-example)Generated Code Example
The following example code demonstrates how the node blends normals in each **Mode** :
**Default**
Adds the x and y components (R and G channels) of the input normals, multiplies the z components (B channel), then normalizes the result.
```
void Unity_NormalBlend_float(float3 A, float3 B, out float3 Out)
{
    Out = normalize(float3(A.rg + B.rg, A.b * B.b));
}

```

**Reoriented**
Blends the input normals using a reoriented method that makes the resulting surface normal look realistic.
```
void Unity_NormalBlend_Reoriented_float(float3 A, float3 B, out float3 Out)
{
    float3 t = A.xyz + float3(0.0, 0.0, 1.0);
    float3 u = B.xyz * float3(-1.0, -1.0, 1.0);
    Out = (t / t.z) * dot(t, u) - u;
}

```



--- Page 88: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-From-Height-Node.html ---

# Normal From Height Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-From-Height-Node.html#description)Description
Creates a normal map from a height value defined by input **Input** with a strength defined by input **Strength**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-From-Height-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Float | Input height value  
Strength | Input | Float | The strength of the output normal. Considered in real-world units, recommended range is 0 - 0.1 .  
Out | Output | Vector 3 | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-From-Height-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Output Space | Dropdown | Tangent, World | Sets the coordinate space of the output normal.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Normal-From-Height-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Output Space** mode.
**Tangent**
```
void Unity_NormalFromHeight_Tangent_float(float In, float Strength, float3 Position, float3x3 TangentMatrix, out float3 Out)
{
    float3 worldDerivativeX = ddx(Position);
    float3 worldDerivativeY = ddy(Position);

    float3 crossX = cross(TangentMatrix[2].xyz, worldDerivativeX);
    float3 crossY = cross(worldDerivativeY, TangentMatrix[2].xyz);
    float d = dot(worldDerivativeX, crossY);
    float sgn = d < 0.0 ? (-1.0f) : 1.0f;
    float surface = sgn / max(0.000000000000001192093f, abs(d));

    float dHdx = ddx(In);
    float dHdy = ddy(In);
    float3 surfGrad = surface * (dHdx*crossY + dHdy*crossX);
    Out = normalize(TangentMatrix[2].xyz - (Strength * surfGrad));
    Out = TransformWorldToTangent(Out, TangentMatrix);
}

```

**World**
```
void Unity_NormalFromHeight_World_float(float In, float Strength, float3 Position, float3x3 TangentMatrix, out float3 Out)
{
    float3 worldDerivativeX = ddx(Position);
    float3 worldDerivativeY = ddy(Position);

    float3 crossX = cross(TangentMatrix[2].xyz, worldDerivativeX);
    float3 crossY = cross(worldDerivativeY, TangentMatrix[2].xyz);
    float d = dot(worldDerivativeX, crossY);
    float sgn = d < 0.0 ? (-1.0f) : 1.0f;
    float surface = sgn / max(0.000000000000001192093f, abs(d));

    float dHdx = ddx(In);
    float dHdy = ddy(In);
    float3 surfGrad = surface * (dHdx*crossY + dHdy*crossX);
    Out = normalize(TangentMatrix[2].xyz - (Strength * surfGrad));
}

```



--- Page 89: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Occlusion-Mapping-Node.html ---

# Parallax Occlusion Mapping Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Occlusion-Mapping-Node.html#description)Description
You can use the Parallax Occlusion Mapping (POM) node to create a parallax effect that displaces a material's UVs and depth to create the illusion of depth inside that material.
If you receive a texture sampling error while using this node in a graph that includes Custom Function nodes or Subgraphs, try upgrading to Shader Graph version 10.3 or later. This may resolve the errors.
When you assign the same Texture2D to a POM node and a Sample Texture 2D node, you need to avoid transforming the UV coordinates twice. To prevent this, connect the Split Texture Transform node’s **Texture Only** port to the Sample Texture 2D Node’s **UV** port.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Occlusion-Mapping-Node.html#ports)Ports
Name | **Direction** | Type | Description  
---|---|---|---  
**Heightmap** | Input | Texture2D | The Texture that specifies the depth of the displacement.  
**Heightmap Sampler** | Input | Sampler State | The Sampler to sample **Heightmap** with.  
**Amplitude** | Input | Float | A multiplier to apply to the height of the **Heightmap** (in centimeters).  
**Steps** | Input | Float | The number of steps that the linear search of the algorithm performs.  
**UVs** | Input | Vector2 | The UVs that the sampler uses to sample the Texture.  
**Tiling** | Input | Vector2 | The tiling to apply to the input UVs.  
**Offset** | Input | Vector2 | The offset to apply to the input UVs.  
**Primitive Size** | Input | Vector2 | Size of the UV space in object space. For example, a Unity built-in Plane mesh has a primitive size of (10,10).  
**LOD** | Input | Float | The level of detail to use to sample the **Heightmap**. This value should always be positive.  
**LOD Threshold** | Input | Float | The **Heightmap** mip level where the Parallax Occlusion Mapping effect begins to fade out. This is equivalent to the **Fading Mip Level Start** property in the High Definition Render Pipeline's (HDRP) [Lit Material](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Lit-Shader.html).  
**Pixel Depth Offset** | Output | Float | The offset to apply to the depth buffer to produce the illusion of depth. Connect this output to the **Depth Offset** on the Master Node to enable effects that rely on the depth buffer, such as shadows and screen space ambient occlusion.  
**Parallax UVs** | Output | Vector2 | UVs that you have added the parallax offset to.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Occlusion-Mapping-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float3 ParallaxOcclusionMapping_ViewDir = IN.TangentSpaceViewDirection * GetDisplacementObjectScale().xzy;
float ParallaxOcclusionMapping_NdotV = ParallaxOcclusionMapping_ViewDir.z;
float ParallaxOcclusionMapping_MaxHeight = Amplitude * 0.01;
ParallaxOcclusionMapping_MaxHeight *= 2.0 / ( abs(Tiling.x) + abs(Tiling.y) );

float2 ParallaxOcclusionMapping_UVSpaceScale = ParallaxOcclusionMapping_MaxHeight * Tiling / PrimitiveSize;

// Transform the view vector into the UV space.
float3 ParallaxOcclusionMapping_ViewDirUV    = normalize(float3(ParallaxOcclusionMapping_ViewDir.xy * ParallaxOcclusionMapping_UVSpaceScale, ParallaxOcclusionMapping_ViewDir.z)); // TODO: skip normalize

PerPixelHeightDisplacementParam ParallaxOcclusionMapping_POM;
ParallaxOcclusionMapping_POM.uv = UVs.xy;

float ParallaxOcclusionMapping_OutHeight;
float2 _ParallaxOcclusionMapping_ParallaxUVs = UVs.xy + ParallaxOcclusionMapping(Lod, Lod_Threshold, Steps, ParallaxOcclusionMapping_ViewDirUV, ParallaxOcclusionMapping_POM, ParallaxOcclusionMapping_OutHeight);

float _ParallaxOcclusionMapping_PixelDepthOffset = (ParallaxOcclusionMapping_MaxHeight - ParallaxOcclusionMapping_OutHeight * ParallaxOcclusionMapping_MaxHeight) / max(ParallaxOcclusionMapping_NdotV, 0.0001);

```



--- Page 90: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Parallax-Mapping-Node.html ---

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



--- Page 91: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polygon-Node.html ---

# Polygon Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polygon-Node.html#description)Description
Generates a regular polygon shape based on input **UV** at the size specified by inputs **Width** and **Height**. The polygon's amount of sides is determined by input **Sides**. The generated shape can be offset or tiled by connecting a [Tiling And Offset Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html). Note that in order to preserve the ability to offset the shape within the UV space the shape will not automatically repeat if tiled. To achieve a repeating polygon effect first connect your input through a [Fraction Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html).
NOTE: This [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can only be used in the **Fragment** shader stage.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polygon-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Sides | Input | Float | None | Amount of sides  
Width | Input | Float | None | Polygon width  
Height | Input | Float | None | Polygon height  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polygon-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Polygon_float(float2 UV, float Sides, float Width, float Height, out float Out)
{
    float pi = 3.14159265359;
    float aWidth = Width * cos(pi / Sides);
    float aHeight = Height * cos(pi / Sides);
    float2 uv = (UV * 2 - 1) / float2(aWidth, aHeight);
    uv.y *= -1;
    float pCoord = atan2(uv.x, uv.y);
    float r = 2 * pi / Sides;
    float distance = cos(floor(0.5 + pCoord / r) * r - pCoord) * length(uv);
    Out = saturate((1 - distance) / fwidth(distance));
}

```



--- Page 92: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polar-Coordinates-Node.html ---

# Polar Coordinates Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polar-Coordinates-Node.html#description)Description
Converts the value of input **UV** to polar coordinates. In mathematics, the polar coordinate system is a two-dimensional coordinate system in which each point on a plane is determined by a distance from a reference point and an angle from a reference direction.
The resulting effect is that the x channel of the input to **UV** is converted to a distance value from the point specified by the value of input **Center** and the y channel of same input is converted to the value of an angle of rotation around that point.
These values can be scaled by the values of inputs **Radial Scale** and **Length Scale** respectively.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polar-Coordinates-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Center | Input | Vector 2 | None | Center reference point  
Radial Scale | Input | Float | None | Scale of distance value  
Length Scale | Input | Float | None | Scale of angle value  
Out | Output | Vector 2 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Polar-Coordinates-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_PolarCoordinates_float(float2 UV, float2 Center, float RadialScale, float LengthScale, out float2 Out)
{
    float2 delta = UV - Center;
    float radius = length(delta) * 2 * RadialScale;
    float angle = atan2(delta.x, delta.y) * 1.0/6.28 * LengthScale;
    Out = float2(radius, angle);
}

```



--- Page 93: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Node.html ---

# Reciprocal Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Node.html#description)Description
Returns the result of dividing 1 by the input **In**. This can be calculated by a fast approximation on Shader Model 5 by setting **Method** to **Fast**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Method | Dropdown | Default, Fast | Selects the method used  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Method** mode.
**Default**
```
void Unity_Reciprocal_float4(float4 In, out float4 Out)
{
    Out = 1.0/In;
}

```

**Fast** (Requires Shader Model 5)
```
void Unity_Reciprocal_Fast_float4(float4 In, out float4 Out)
{
    Out = rcp(In);
}

```



--- Page 94: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Position-Node.html ---

# Position node
The Position node returns the position of a vertex or fragment of a mesh.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Position-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**Out** | Output | Vector 3 | None | Position of the vertex or fragment of the mesh, depending on the [shader stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html) of the graph section.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Position-Node.html#space)Space
The **Space** dropdown determines the coordinate space of the output position.
**Options** | **Description**  
---|---  
**Object** | Returns the vertex or fragment position relative to the origin of the object.  
**View** | Returns the vertex or fragment position relative to the camera, in meters.  
**World** | Returns the vertex or fragment position in the world, in meters. If you use the High Definition Render Pipeline (HDRP), **World** returns the position [relative to the camera](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?preview=1&subfolder=/manual/Camera-Relative-Rendering.html).  
**Tangent** | Returns the vertex or fragment position relative to the tangent of the surface, in meters. For more information, refer to [Normal maps](https://docs.unity3d.com/6000.3/Documentation/Manual/StandardShaderMaterialParameterNormalMapLanding.html).  
**Absolute World** | Returns the vertex or fragment position in the world, in meters.


--- Page 95: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Power-Node.html ---

# Power Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Power-Node.html#description)Description
Returns the result of input **A** to the power of input **B**.
Note: If the input **A** is negative, the output might be inconsistent or NaN.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Power-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Power-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Power_float4(float4 A, float4 B, out float4 Out)
{
    Out = pow(A, B);
}

```



--- Page 96: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Posterize-Node.html ---

# Posterize Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Posterize-Node.html#description)Description
> Posterization or posterisation of an image entails conversion of a continuous gradation of tone to several regions of fewer tones, with abrupt changes from one tone to another.
_<https://en.wikipedia.org/wiki/Posterization>_
This node returns the posterized (also known as quantized) value of the input **In** into an amount of values specified by input **Steps**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Posterize-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Steps | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Posterize-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Posterize_float4(float4 In, float4 Steps, out float4 Out)
{
    Out = floor(In * Steps) / Steps;
}

```



--- Page 97: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Random-Range-Node.html ---

# Random Range Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Random-Range-Node.html#description)Description
Returns a pseudo-random number value based on input **Seed** that is between the minimum and maximum values defined by inputs **Min** and **Max** respectively.
Whilst the same value in input **Seed** will always result in the same output value, the output value itself will appear random. Input **Seed** is a **Vector 2** value for the convenience of generating a random number based on a UV input, however for most cases a **Float** input will suffice.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Random-Range-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Seed | Input | Vector 2 | Seed value used for generation  
Min | Input | Float | Minimum value  
Max | Input | Float | Maximum value  
Out | Output | Float | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Random-Range-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_RandomRange_float(float2 Seed, float Min, float Max, out float Out)
{
    float randomno =  frac(sin(dot(Seed, float2(12.9898, 78.233)))*43758.5453);
    Out = lerp(Min, Max, randomno);
}

```



--- Page 98: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rectangle-Node.html ---

# Rectangle Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rectangle-Node.html#description)Description
Generates a rectangle shape based on input **UV** at the size specified by inputs **Width** and **Height**. The generated shape can be offset or tiled by connecting a [Tiling And Offset Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html). Note that in order to preserve the ability to offset the shape within the UV space the shape will not automatically repeat if tiled. To achieve a repeating rectangle effect first connect your input through a [Fraction Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html).
NOTE: This [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can only be used in the **Fragment** [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rectangle-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Width | Input | Float | None | Rectangle width  
Height | Input | Float | None | Rectangle height  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rectangle-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Dropdown | Fastest, Nicest | Robustness of computation  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rectangle-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Rectangle_float(float2 UV, float Width, float Height, out float Out)
{
    float2 d = abs(UV * 2 - 1) - float2(Width, Height);
    d = 1 - d / fwidth(d);
    Out = saturate(min(d.x, d.y));
}

```



--- Page 99: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Probe-Node.html ---

# Reflection Probe Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Probe-Node.html#description)Description
Provides access to the nearest **Reflection Probe** to the object. Requires **Normal** and **View Direction** to sample the probe. You can achieve a blurring effect by sampling at a different Level of Detail using the **LOD** input.
Note: The behavior of this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined globally. Shader Graph does not define the function of the node. Instead, each Render Pipeline defines what HLSL code to execute for this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html).
Different Render Pipelines may produce different results. If you're building a shader in one Render Pipeline that you want to use in both, try checking it in both pipelines before production. A [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) might be defined in one Render Pipeline and undefined in the other. If this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) is undefined, it returns 0 (black).
####  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Probe-Node.html#unity-render-pipelines-support)Unity Render Pipelines Support
  * Universal Render Pipeline


The High Definition Render Pipeline does **not** support this Node.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Probe-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
View Dir | Input | Vector 3 | View Direction (object space) | Mesh's view direction  
Normal | Input | Vector 3 | Normal (object space) | Mesh's normal vector  
LOD | Input | Float | None | Level of detail for sampling  
Out | Output | Vector 3 | None | Output color value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reflection-Probe-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_ReflectionProbe_float(float3 ViewDir, float3 Normal, float LOD, out float3 Out)
{
    Out = SHADERGRAPH_REFLECTION_PROBE(ViewDir, Normal, LOD);
}

```



--- Page 100: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Preview-Node.html ---

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



--- Page 101: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Radial-Shear-Node.html ---

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



--- Page 102: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Square-Root-Node.html ---

# Reciprocal Square Root Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Square-Root-Node.html#description)Description
Returns the result of 1 divided by the square root of the input **In**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Square-Root-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Reciprocal-Square-Root-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_ReciprocalSquareRoot_float4(float4 In, out float4 Out)
{
    Out = rsqrt(In);
}

```



--- Page 103: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Round-Node.html ---

# Round Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Round-Node.html#description)Description
Returns the value of input **In** rounded to the nearest integer, or whole number.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Round-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Round-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Round_float4(float4 In, out float4 Out)
{
    Out = round(In);
}

```



--- Page 104: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Remap-Node.html ---

# Remap node
The Remap node converts a value from one range to another, which is also known as linear interpolation. For example, you can use the node to convert a value in the range 0 to 1 to the equivalent value in the range 0 to 100.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Remap-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Description**  
---|---|---|---  
**In** | Input | Dynamic Vector | The value to convert.  
**In Min Max** | Input | Vector 2 | The original minimum and maximum range of **In**.  
**Out Min Max** | Input | Vector 2 | The new minimum and maximum range to use to interpolate **In**.  
**Out** | Output | Dynamic Vector | The converted value.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Remap-Node.html#generated-code-example)Generated code example
The following example code represents one possible outcome of this node.
```
void Unity_Remap_float4(float4 In, float2 InMinMax, float2 OutMinMax, out float4 Out)
{
    Out = OutMinMax.x + (In - InMinMax.x) * (OutMinMax.y - OutMinMax.x) / (InMinMax.y - InMinMax.x);
}

```



--- Page 105: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturation-Node.html ---

# Saturation Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturation-Node.html#description)Description
Adjusts the saturation of input **In** by the amount of input **Saturation**. A **Saturation** value of 1 will return the input unaltered. A **Saturation** value of 0 will return the input completely desaturated.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturation-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value  
Saturation | Input | Float | None | Saturation value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturation-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Saturation_float(float3 In, float Saturation, out float3 Out)
{
    float luma = dot(In, float3(0.2126729, 0.7151522, 0.0721750));
    Out =  luma.xxx + Saturation.xxx * (In - luma.xxx);
}

```



--- Page 106: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Rectangle-Node.html ---

# Rounded Rectangle Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Rectangle-Node.html#description)Description
Generates a rounded rectangle shape based on input **UV** at the size specified by inputs **Width** and **Height**. The radius of each corner is defined by input **Radius**. The generated shape can be offset or tiled by connecting a [Tiling And Offset Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html). Note that in order to preserve the ability to offset the shape within the UV space the shape will not automatically repeat if tiled. To achieve a repeating rounded rectangle effect first connect your input through a [Fraction Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html).
NOTE: This [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can only be used in the **Fragment** [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Rectangle-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Width | Input | Float | None | Rounded Rectangle width  
Height | Input | Float | None | Rounded Rectangle height  
Radius | Input | Float | None | Corner radius  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Rectangle-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_RoundedRectangle_float(float2 UV, float Width, float Height, float Radius, out float Out)
{
    Radius = max(min(min(abs(Radius * 2), abs(Width)), abs(Height)), 1e-5);
    float2 uv = abs(UV * 2 - 1) - float2(Width, Height) + Radius;
    float d = length(max(0, uv)) / Radius;
    Out = saturate((1 - d) / fwidth(d));
}

```



--- Page 107: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Slider-Node.html ---

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



--- Page 108: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Polygon-Node.html ---

# Rounded Polygon Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Polygon-Node.html#description)Description
Generates a rounded polygon shape based on input **UV** at the size specified by inputs **Width** and **Height**. The input **Sides** specifies the number of sides, and the input **Roundness** defines the roundness of each corner.
You can connect a [Tiling And Offset Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html) to offset or tile the shape. To preserve the ability to offset the shape within the UV space, the shape does not automatically repeat if you tile it. To achieve a repeating rounded polygon effect, first connect your **UV** input through a [Fraction Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Fraction-Node.html).
You can only use the Rounded Polygon Node in the **Fragment** [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Polygon-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Width | Input | Float | None | Rounded Polygon width  
Height | Input | Float | None | Rounded Polygon height  
Sides | Input | Float | None | Number of sides of the polygon  
Roundness | Input | Float | None | Roundness of corners  
Out | Output | Float | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rounded-Polygon-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void RoundedPolygon_Func_float(float2 UV, float Width, float Height, float Sides, float Roundness, out float Out)
{
    UV = UV * 2. + float2(-1.,-1.);
    float epsilon = 1e-6;
    UV.x = UV.x / ( Width + (Width==0)*epsilon);
    UV.y = UV.y / ( Height + (Height==0)*epsilon);
    Roundness = clamp(Roundness, 1e-6, 1.);
    float i_sides = floor( abs( Sides ) );
    float fullAngle = 2. * PI / i_sides;
    float halfAngle = fullAngle / 2.;
    float opositeAngle = HALF_PI - halfAngle;
    float diagonal = 1. / cos( halfAngle );
    // Chamfer values
    float chamferAngle = Roundness * halfAngle; // Angle taken by the chamfer
    float remainingAngle = halfAngle - chamferAngle; // Angle that remains
    float ratio = tan(remainingAngle) / tan(halfAngle); // This is the ratio between the length of the polygon's triangle and the distance of the chamfer center to the polygon center
    // Center of the chamfer arc
    float2 chamferCenter = float2(
        cos(halfAngle) ,
        sin(halfAngle)
    )* ratio * diagonal;
    // starting of the chamfer arc
    float2 chamferOrigin = float2(
        1.,
        tan(remainingAngle)
    );
    // Using Al Kashi algebra, we determine:
    // The distance distance of the center of the chamfer to the center of the polygon (side A)
    float distA = length(chamferCenter);
    // The radius of the chamfer (side B)
    float distB = 1. - chamferCenter.x;
    // The refence length of side C, which is the distance to the chamfer start
    float distCref = length(chamferOrigin);
    // This will rescale the chamfered polygon to fit the uv space
    // diagonal = length(chamferCenter) + distB;
    float uvScale = diagonal;
    UV *= uvScale;
    float2 polaruv = float2 (
        atan2( UV.y, UV.x ),
        length(UV)
    );
    polaruv.x += HALF_PI + 2*PI;
    polaruv.x = fmod( polaruv.x + halfAngle, fullAngle );
    polaruv.x = abs(polaruv.x - halfAngle);
    UV = float2( cos(polaruv.x), sin(polaruv.x) ) * polaruv.y;
    // Calculate the angle needed for the Al Kashi algebra
    float angleRatio = 1. - (polaruv.x-remainingAngle) / chamferAngle;
    // Calculate the distance of the polygon center to the chamfer extremity
    float distC = sqrt( distA*distA + distB*distB - 2.*distA*distB*cos( PI - halfAngle * angleRatio ) );
    Out = UV.x;
    float chamferZone = ( halfAngle - polaruv.x ) < chamferAngle;
    Out = lerp( UV.x, polaruv.y / distC, chamferZone );
    // Output this to have the shape mask instead of the distance field
    Out = saturate((1 - Out) / fwidth(Out));
}

```



--- Page 109: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Replace-Color-Node.html ---

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



--- Page 110: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Spherize-Node.html ---

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



--- Page 111: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturate-Node.html ---

# Saturate Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturate-Node.html#description)Description
Returns the value of input **In** clamped between 0 and 1.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturate-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Saturate-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Saturate_float4(float4 In, out float4 Out)
{
    Out = saturate(In);
}

```



--- Page 112: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Gradient-Node.html ---

# Sample Gradient Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Gradient-Node.html#description)Description
Samples a **Gradient** given the input of **Time**. Returns a **Vector 4** color value for use in the shader.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Gradient-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Gradient | Input | Gradient | None | Gradient to sample  
Time | Input | Float | None | Point at which to sample gradient (0.0–1.0)  
Out | Output | Vector 4 | None | Output value as Vector4  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Gradient-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_SampleGradient_float(float4 Gradient, float Time, out float4 Out)
{
    float3 color = Gradient.colors[0].rgb;
    [unroll]
    for (int c = 1; c < 8; c++)
    {
        float colorPos = saturate((Time - Gradient.colors[c-1].w) / (Gradient.colors[c].w - Gradient.colors[c-1].w)) * step(c, Gradient.colorsLength-1);
        color = lerp(color, Gradient.colors[c].rgb, lerp(colorPos, step(0.01, colorPos), Gradient.type));
    }
#ifndef UNITY_COLORSPACE_GAMMA
    color = SRGBToLinear(color);
#endif
    float alpha = Gradient.alphas[0].x;
    [unroll]
    for (int a = 1; a < 8; a++)
    {
        float alphaPos = saturate((Time - Gradient.alphas[a-1].y) / (Gradient.alphas[a].y - Gradient.alphas[a-1].y)) * step(a, Gradient.alphasLength-1);
        alpha = lerp(alpha, Gradient.alphas[a].x, lerp(alphaPos, step(0.01, alphaPos), Gradient.type));
    }
    Out = float4(color, alpha);
}

```



--- Page 113: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html ---

# Screen Position Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html#description)Description
Provides access to the screen position of the mesh vertex or fragment. The X and Y values represent the horizontal and vertical positions respectively. Use the **Mode** dropdown control to select the mode of the output value. The available modes are as follows:
  * **Default** - Returns X and Y values that represent the normalized **Screen Position**. The normalized **Screen Position** is the **Screen Position** divided by the clip space position W component. The X and Y value ranges are between 0 and 1 with position `float2(0,0)` at the lower left corner of the screen. The Z and W values aren't used in this mode, so they're always 0.
  * **Raw** - Returns the raw **Screen Position** values, which are the **Screen Position** values before the clip space position W component is divided out. Position `float2(0,0)` is at the lower left corner of the screen. This mode is useful for projection.
  * **Center** - Returns X and Y values that represent the normalized **Screen Position** offset so position `float2(0,0)` is at the center of the screen. The range of the X and Y values is –1 to 1. The Z and W values aren't used in this mode, so they're always 0.
  * **Tiled** - Returns **Screen Position** offset so position `float2(0,0)` is at the center of the screen and tiled using `frac`.
  * **Pixel** - Returns **Screen Position** in terms of the actual pixel width and height values of the screen. In this mode, position `float2(0,0)` is at the lower left corner of the screen. Whereas the range of Default mode is always 0 to 1, the range of Pixel mode depends on the screen resolution. The Z and W values aren't used in this mode, so they're always 0.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 4 | None | Get the **Screen Position** of the mesh.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Mode | Dropdown | Default, Raw, Center, Tiled, Pixel | Select which coordinate space to use for the **Screen Position** output.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Screen-Position-Node.html#generated-code-example)Generated Code Example
The following code examples represent one possible outcome for each mode.
**Default**
```
float4 Out = float4(IN.NDCPosition.xy, 0, 0);

```

**Raw**
```
float4 Out = IN.ScreenPosition;

```

**Center**
```
float4 Out = float4(IN.NDCPosition.xy * 2 - 1, 0, 0);

```

**Tiled**
```
float4 Out = frac(float4((IN.NDCPosition.x * 2 - 1) * _ScreenParams.x / _ScreenParams.y, IN.{0}.y * 2 - 1, 0, 0));

```

**Pixel**
```
float4 Out = float4(IN.PixelPosition.xy, 0, 0);

```



--- Page 114: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sign-Node.html ---

# Sign Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sign-Node.html#description)Description
Per component, returns -1 if the value of input **In** is less than zero, 0 if equal to zero and 1 if greater than zero.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sign-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sign-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Sign_float4(float4 In, out float4 Out)
{
    Out = sign(In);
}

```



--- Page 115: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Smoothstep-Node.html ---

# Smoothstep Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Smoothstep-Node.html#description)Description
Returns the result of a smooth Hermite interpolation between 0 and 1, if the value of input **In** is between the values of inputs **Edge1** and **Edge2** respectively. Returns 0 if the value of input **In** is less than the value of input **Edge1** and 1 if greater than the value of input **Edge2**.
The Smoothstep node is similar to the [Lerp Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html) but there are two notable differences. Firstly, with the Smoothstep node, the user specifies the range and the return value is between 0 and 1. You can consider this the opposite of the [Lerp Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Lerp-Node.html). Secondly, the Smoothstep node uses smooth Hermite interpolation instead of linear interpolation, which means the interpolation gradually speeds up from the start and slows down toward the end. This interpolation is useful for creating natural-looking animation, fading, and other transitions.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Smoothstep-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Edge1 | Input | Dynamic Vector | Minimum step value  
Edge2 | Input | Dynamic Vector | Maximum step value  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Smoothstep-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Smoothstep_float4(float4 Edge1, float4 Edge2, float4 In, out float4 Out)
{
    Out = smoothstep(Edge1, Edge2, In);
}

```



--- Page 116: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-Node.html ---

# Rotate Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-Node.html#description)Description
Rotates value of input **UV** around a reference point defined by input **Center** by the amount of input **Rotation**. The unit for rotation angle can be selected by the parameter **Unit**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Center | Input | Vector 2 | None | Center point to rotate around  
Rotation | Input | Float | None | Amount of rotation to apply  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Unit | Dropdown | Radians, Degrees | Switches the unit for input **Rotation**  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Rotate-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per **Unit** mode.
**Radians**
```
void Unity_Rotate_Radians_float(float2 UV, float2 Center, float Rotation, out float2 Out)
{
    UV -= Center;
    float s, c;
    sincos(Rotation, s, c);
    float3 r3 = float(-s, c, s);
    float2 r1;
    r1.y = dot(UV, r3.xy);
    r1.x = dot(UV, r3.yz);
    Out = r1 + Center;
}

```

**Degrees**
```
void Unity_Rotate_Degrees_float(float2 UV, float2 Center, float Rotation, out float2 Out)
{
    Rotation = Rotation * (3.1415926f/180.0f);
    UV -= Center;
    float s, c;
    sincos(Rotation, s, c);
    float3 r3 = float(-s, c, s);
    float2 r1;
    r1.y = dot(UV, r3.xy);
    r1.x = dot(UV, r3.yz);
    Out = r1 + Center;
}

```



--- Page 117: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Simple-Noise-Node.html ---

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



--- Page 118: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Color-Node.html ---

# Scene Color node
The Scene Color node samples the color buffer of the current camera, using the screen space coordinates you input.
If you use the Universal Render Pipeline (URP), the node samples the opaque texture, which is a copy of the color buffer before Unity renders transparent objects. For more information, refer to [Universal Render Pipeline asset reference](https://docs.unity3d.com/Manual/urp/universalrp-asset.html).
To make sure the Scene Color node outputs the correct values, follow these steps:
  1. Connect the node to the fragment [shader stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html). The Scene Color node doesn't support the vertex shader stage.
  2. In the **Graph Settings** tab of the [**Graph Inspector**](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Internal-Inspector.html) window, set **Surface Type** to **Transparent**. Otherwise, the node samples the color buffer before Unity renders all the opaque contents in the scene.


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Color-Node.html#render-pipeline-support)Render pipeline support
The Scene Color node supports the following render pipelines:
  * Universal Render Pipeline (URP)
  * High Definition Render Pipeline (HDRP)


If you use the Scene Color node with an unsupported pipeline, it returns 0 (black).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Color-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**UV** | Input | Vector 4 | Screen position | The normalized screen space coordinates to sample from.  
**Out** | Output | Vector 3 | None | The color value from the color buffer at the **UV** coordinates.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Color-Node.html#generated-code-example)Generated code example
The HLSL code this node generates depends on the render pipeline you use. If you use your own custom render pipeline, you must define the behavior of the node yourself. Otherwise, the node returns a value of 0 (black).
The following example code represents one possible outcome of this node.
```
void Unity_SceneColor_float(float4 UV, out float3 Out)
{
    Out = SHADERGRAPH_SAMPLE_SCENE_COLOR(UV);
}

```



--- Page 119: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Depth-Node.html ---

# Scene Depth node
The Scene Depth node samples the depth texture of the current camera, using the screen space coordinates you input. The node returns the depth of the closest object the camera sees along the path towards the coordinates, or 1 (white) if no object is present.
If you use the Universal Render Pipeline (URP), make sure the depth texture is enabled in the [URP asset](https://docs.unity3d.com/Manual/urp/universalrp-asset.html). Otherwise the Scene Depth node returns a value of 0.5 (mid-grey).
The Scene Depth node works only in the fragment [shader stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html), and might not work if you set **Surface Type** to **Opaque** in the **Graph Inspector** window.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Depth-Node.html#render-pipeline-support)Render pipeline support
This node supports the following render pipelines:
  * High Definition Render Pipeline (HDRP)
  * Universal Render Pipeline (URP)


##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Depth-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**UV** | Input | Vector 4 | Screen position | The normalized screen space coordinates to sample from.  
**Out** | Output | Float | None | The depth value from the depth texture at the **UV** coordinates.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Depth-Node.html#sampling-modes)Sampling modes
**Name** | **Description**  
---|---  
**Linear 01** | Returns the linear depth value. The range is from 0 to 1. 0 is the near clipping plane of the camera, and 1 is the far clipping plane of the camera.  
**Raw** | Returns the non-linear depth value. The range is from 0 to 1. 0 is the near clipping plane of the camera, and 1 is the far clipping plane of the camera.  
**Eye** | Returns the depth value as the distance from the camera in meters.  
For more information about clipping planes, refer to [Introduction to the camera view](https://docs.unity3d.com/Manual/UnderstandingFrustum.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Scene-Depth-Node.html#generated-code-example)Generated code example
The HLSL code this node generates depends on the render pipeline you use. If you use your own custom render pipeline, you must define the behaviour of the node yourself, otherwise the node returns a value of 1 (white).
The following example code represents one possible outcome of this node.
```
void Unity_SceneDepth_Raw_float(float4 UV, out float Out)
{
    Out = SHADERGRAPH_SAMPLE_SCENE_DEPTH(UV);
}

```



--- Page 120: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Square-Root-Node.html ---

# Square Root Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Square-Root-Node.html#description)Description
Returns the square root of input **In**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Square-Root-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Square-Root-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_SquareRoot_float4(float4 In, out float4 Out)
{
    Out = sqrt(In);
}

```



--- Page 121: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Split-Node.html ---

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



--- Page 122: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sprite-Skinning-Node.html ---

# Sprite Skinning Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sprite-Skinning-Node.html#description)Description
This node lets you apply Vertex Skinning, and only works with the [2D Animation](https://docs.unity3d.com/Packages/com.unity.2d.animation@latest/). You must use the [SpriteSkin](https://docs.unity3d.com/Packages/com.unity.2d.animation@latest?subfolder=/manual/SpriteSkin.html) component provided with the 2D Animation Package.  
Please ensure the following settings are enabled:  
1. GPU Skinning is enabled in Player/Rendering/GPU Skinning in Project Settings.  
2. SRP-Batcher enabled in RenderpipelineAsset.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sprite-Skinning-Node.html#ports)Ports
Name | Direction | Type | Stage | Description  
---|---|---|---|---  
Position | Input | Vector3 | Vertex | Position of the vertex in object space.  
Normal | Input | Vector3 | Vertex | Normal of the vertex in object space.  
Tangent | Input | Vector3 | Vertex | Tangent of the vertex in object space.  
Position | Output | Vector3 | Vertex | Outputs the skinned vertex position.  
Normal | Output | Vector3 | Vertex | Outputs the skinned vertex normal.  
Tangent | Output | Vector3 | Vertex | Outputs the skinned vertex tangent.


--- Page 123: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Step-Node.html ---

# Step Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Step-Node.html#description)Description
Per component, returns 1 if the value of input **In** is greater than or equal to the value of input **Edge** , otherwise returns 0.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Step-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
Edge | Input | Dynamic Vector | Step value  
In | Input | Dynamic Vector | Input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Step-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Step_float4(float4 Edge, float4 In, out float4 Out)
{
    Out = step(Edge, In);
}

```



--- Page 124: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html ---

# Tiling And Offset Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html#description)Description
Tiles and offsets the value of input **UV** by the inputs **Tiling** and **Offset** respectively. This is commonly used for detail maps and scrolling textures over [Time](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Tiling | Input | Vector 2 | None | Amount of tiling to apply per channel  
Offset | Input | Vector 2 | None | Amount of offset to apply per channel  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tiling-And-Offset-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_TilingAndOffset_float(float2 UV, float2 Tiling, float2 Offset, out float2 Out)
{
    Out = UV * Tiling + Offset;
}

```



--- Page 125: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-ID-Node.html ---

# Vertex ID Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-ID-Node.html#description)Description
Provides access to the mesh vertex or fragment's **Vertex ID** value.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-ID-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Float | None |  **Vertex ID** for the Mesh Vertex/Fragment.


--- Page 126: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/White-Balance-Node.html ---

# White Balance Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/White-Balance-Node.html#description)Description
Adjusts the temperature and tint of input **In** by the amount of inputs **Temperature** and **Tint** respectively. **Temperature** has the effect of shifting the values towards yellow or blue. **Tint** has the effect of shifting towards pink or green.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/White-Balance-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
In | Input | Vector 3 | None | Input value  
Temperature | Input | Float | None | Temperature offset value  
Tint | Input | Float | None | Tint offset value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/White-Balance-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_WhiteBalance_float(float3 In, float Temperature, float Tint, out float3 Out)
{
    // Range ~[-1.67;1.67] works best
    float t1 = Temperature * 10 / 6;
    float t2 = Tint * 10 / 6;

    // Get the CIE xy chromaticity of the reference white point.
    // Note: 0.31271 = x value on the D65 white point
    float x = 0.31271 - t1 * (t1 < 0 ? 0.1 : 0.05);
    float standardIlluminantY = 2.87 * x - 3 * x * x - 0.27509507;
    float y = standardIlluminantY + t2 * 0.05;

    // Calculate the coefficients in the LMS space.
    float3 w1 = float3(0.949237, 1.03542, 1.08728); // D65 white point

    // CIExyToLMS
    float Y = 1;
    float X = Y * x / y;
    float Z = Y * (1 - x - y) / y;
    float L = 0.7328 * X + 0.4296 * Y - 0.1624 * Z;
    float M = -0.7036 * X + 1.6975 * Y + 0.0061 * Z;
    float S = 0.0030 * X + 0.0136 * Y + 0.9834 * Z;
    float3 w2 = float3(L, M, S);

    float3 balance = float3(w1.x / w2.x, w1.y / w2.y, w1.z / w2.z);

    float3x3 LIN_2_LMS_MAT = {
        3.90405e-1, 5.49941e-1, 8.92632e-3,
        7.08416e-2, 9.63172e-1, 1.35775e-3,
        2.31082e-2, 1.28021e-1, 9.36245e-1
    };

    float3x3 LMS_2_LIN_MAT = {
        2.85847e+0, -1.62879e+0, -2.48910e-2,
        -2.10182e-1,  1.15820e+0,  3.24281e-4,
        -4.18120e-2, -1.18169e-1,  1.06867e+0
    };

    float3 lms = mul(LIN_2_LMS_MAT, In);
    lms *= balance;
    Out = mul(LMS_2_LIN_MAT, lms);
}

```



--- Page 127: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transformation-Matrix-Node.html ---

# Transformation Matrix Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transformation-Matrix-Node.html#description)Description
Defines a constant **Matrix 4x4** value for a common **Transformation Matrix** in the shader. The **Transformation Matrix** can be selected from the dropdown parameter.
Two output value options for this node, **Inverse Projection** and **Inverse View Projection** , are not compatible with the Built-In Render Pipeline target. When you choose either of these options and target the Built-In Render Pipeline, this node produces an entirely black result.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transformation-Matrix-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Matrix 4 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transformation-Matrix-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
| Dropdown | Model, InverseModel, View, InverseView, Projection, InverseProjection, ViewProjection, InverseViewProjection | Sets output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Transformation-Matrix-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node per mode.
**Model**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_M;

```

**InverseModel**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_I_M;

```

**View**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_V;

```

**InverseView**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_I_V;

```

**Projection**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_P;

```

**InverseProjection**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_I_P;

```

**ViewProjection**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_VP;

```

**InverseViewProjection**
```
float4x4 _TransformationMatrix_Out = UNITY_MATRIX_I_VP;

```



--- Page 128: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tangent-Vector-Node.html ---

##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tangent-Vector-Node.html#description)Description
Provides access to the mesh vertex or fragment's **Tangent Vector**. The coordinate space of the output value can be selected with the **Space** dropdown parameter.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tangent-Vector-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 3 | None | Mesh's **Tangent Vector**.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Tangent-Vector-Node.html#parameters)Parameters
Name | Type | Options | Description  
---|---|---|---  
Space | Dropdown | Object, View, World, Tangent | Selects coordinate space of **Tangent Vector** to output.


--- Page 129: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Voronoi-Node.html ---

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



--- Page 130: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-Color-Node.html ---

# Vertex Color Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-Color-Node.html#description)Description
Provides access to the mesh vertex or fragment's **Vertex Color** value.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vertex-Color-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 4 | None |  **Vertex Color** for the Mesh Vertex/Fragment.


--- Page 131: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Twirl-Node.html ---

# Twirl Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Twirl-Node.html#description)Description
Applies a twirl warping effect similar to a black hole to the value of input **UV**. The center reference point of the warping effect is defined by input **Center** and the overall strength of the effect is defined by the value of input **Strength**. Input **Offset** can be used to offset the individual channels of the result.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Twirl-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
UV | Input | Vector 2 | UV | Input UV value  
Center | Input | Vector 2 | None | Center reference point  
Strength | Input | Float | None | Strength of the effect  
Offset | Input | Vector 2 | None | Individual channel offsets  
Out | Output | Vector 2 | None | Output UV value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Twirl-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Twirl_float(float2 UV, float2 Center, float Strength, float2 Offset, out float2 Out)
{
    float2 delta = UV - Center;
    float angle = Strength * length(delta);
    float x = cos(angle) * delta.x - sin(angle) * delta.y;
    float y = sin(angle) * delta.x + cos(angle) * delta.y;
    Out = float2(x + Center.x + Offset.x, y + Center.y + Offset.y);
}

```



--- Page 132: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Subtract-Node.html ---

# Subtract Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Subtract-Node.html#description)Description
Returns the result of input **A** minus input **B**.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Subtract-Node.html#ports)Ports
Name | Direction | Type | Description  
---|---|---|---  
A | Input | Dynamic Vector | First input value  
B | Input | Dynamic Vector | Second input value  
Out | Output | Dynamic Vector | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Subtract-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
void Unity_Subtract_float4(float4 A, float4 B, out float4 Out)
{
    Out = A - B;
}

```



--- Page 133: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html ---

# Time Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html#description)Description
Provides access to various **Time** parameters in the shader.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Time | Output | Float | None | Elapsed time in seconds.  
Sine Time | Output | Float | None | Sine of the **Time** value. Output ranges from −1 to 1.  
Cosine Time | Output | Float | None | Cosine of the **Time** value. Output ranges from −1 to 1.  
Delta Time | Output | Float | None | The time that has elapsed between the current frame and the last frame, in seconds.  
Smooth Delta | Output | Float | None | The time that has elapsed between the current frame and the last frame, in seconds, averaged over several frames to reduce jitter.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Time-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float Time_Time = _Time.y;
float Time_SineTime = _SinTime.w;
float Time_CosineTime = _CosTime.w;
float Time_DeltaTime = unity_DeltaTime.x;
float Time_SmoothDelta = unity_DeltaTime.z;

```



--- Page 134: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Triplanar-Node.html ---

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



--- Page 135: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Node.html ---

# UV node
The UV node outputs the vertex or fragment UV coordinates of a mesh.
UV coordinates usually have two channels, but the UV node outputs four channels so you can use the remaining two channels, for example to store custom mesh data.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Node.html#ports)Ports
**Name** | **Direction** | **Type** | **Binding** | **Description**  
---|---|---|---|---  
**Out** | Output | Vector 4 | None | The u and v coordinates from the mesh in the first two channels, and two extra channels.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/UV-Node.html#controls)Controls
**Name** | **Type** | **Options** | **Description**  
---|---|---|---  
**Channel** | Dropdown |  **UV0** , **UV1** , **UV2** , **UV3** , **UV4** , **UV5** , **UV6** , **UV7** | Selects the coordinate set to output.


--- Page 136: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html ---

# Subgraph node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html#description)Description
Provides a reference to a [Subgraph Asset](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Asset.html). All ports on the reference node are defined by the properties and outputs defined in the Subgraph Asset. This is useful for sharing functionality between graphs or duplicating the same functionality within a graph.
The preview used for a Subgraph Node is determined by the first port of that [Subgraph](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph.html) Output node. Valid [Data Types](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Data-Types.html) for the first port are `Float`, `Vector 2`, `Vector 3`, `Vector 4`, `Matrix2`, `Matrix3`, `Matrix4`, and `Boolean`. Any other data type will produce an error in the preview shader and the Subgraph will become invalid.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sub-graph-Node.html#subgraph-nodes-and-shader-stages)Subgraph Nodes and Shader Stages
If a [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) within a Subgraph specifies a [Shader Stage](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Shader-Stage.html), such as how [Sample Texture 2D Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Sample-Texture-2D-Node.html) specifies the **fragment** Shader Stage, then that entire Subgraph) is now locked to that stage. As such a Subgraph node that references the graph will also be locked to that Shader Stage.
Furthermore, when an [Edge](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) connected to an output [Port](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) on a **Subgraph Node** flows into a port on the [Master Stack](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Master-Stack.html) that **Subgraph Node** is now locked to the Shader Stage of that [Block Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Block-Node.html) in the Master Stack.


--- Page 137: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/View-Direction-Node.html ---

# View Direction Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/View-Direction-Node.html#description)Description
Provides access to the mesh vertex or fragment's **View Direction** vector. This is the vector from the vertex or fragment to the camera. Select a **Space** to modify the coordinate space of the output value.
Prior to version 11.0, the **View Direction Node** works differently in HDRP than in URP. In URP, it only stored Object space vectors normalized. HDRP stores all vectors normalized.
From 11.0 onwards, this node stores all vectors normalized in both the **High-Definition Render Pipeline** and the **Universal Render Pipeline**.
If you want to keep using the old behavior in URP outside of object space, replace this node with a [View Vector Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/View-Vector-Node.html).
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/View-Direction-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
Out | Output | Vector 3 | None | View Vector for the Mesh Vertex/Fragment.  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/View-Direction-Node.html#controls)Controls
Name | Type | Options | Description  
---|---|---|---  
Space | Dropdown | Object, View, World, Tangent | Selects coordinate space of **View Direction** to output.


--- Page 138: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-2-Node.html ---

# Vector 2 Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-2-Node.html#description)Description
Defines a **Vector 2** value in the shader. If [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **X** and **Y** are not connected with [Edges](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) defines a constant **Vector 2** , otherwise this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can be used to combine various **Float** values.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-2-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
X | Input | Float | None | Input x component value  
Y | Input | Float | None | Input y component value  
Out | Output | Vector 2 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-2-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float2 _Vector2_Out = float2(X, Y);

```



--- Page 139: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-4-Node.html ---

# Vector 4 Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-4-Node.html#description)Description
Defines a **Vector 4** value in the shader. If [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **X** , **Y** , **Z** and **W** are not connected with [Edges](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) defines a constant **Vector 4** , otherwise this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can be used to combine various **Float** values.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-4-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
X | Input | Float | None | Input x component value  
Y | Input | Float | None | Input y component value  
Z | Input | Float | None | Input z component value  
W | Input | Float | None | Input w component value  
Out | Output | Vector 4 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-4-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float4 _Vector4_Out = float4(X, Y, Z, W);

```



--- Page 140: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Swizzle-Node.html ---

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



--- Page 141: https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-3-Node.html ---

# Vector 3 Node
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-3-Node.html#description)Description
Defines a **Vector 3** value in the shader. If [Ports](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Port.html) **X** , **Y** and **Z** are not connected with [Edges](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Edge.html) this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) defines a constant **Vector 3** , otherwise this [Node](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Node.html) can be used to combine various **Float** values.
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-3-Node.html#ports)Ports
Name | Direction | Type | Binding | Description  
---|---|---|---|---  
X | Input | Float | None | Input x component value  
Y | Input | Float | None | Input y component value  
Z | Input | Float | None | Input z component value  
Out | Output | Vector 3 | None | Output value  
##  [](https://docs.unity3d.com/Packages/com.unity.shadergraph%4017.4/manual/Vector-3-Node.html#generated-code-example)Generated Code Example
The following example code represents one possible outcome of this node.
```
float3 _Vector3_Out = float3(X, Y, Z);

```


