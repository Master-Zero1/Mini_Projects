<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Color Image to Grayscale Converter</title>
</head>

<body>

<h1 align="center">Color Image to Grayscale Converter</h1>

<p align="center">
  <img src="https://via.placeholder.com/800x200.png?text=Grayscale+Image+Processing" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue">
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/Project-Beginner--to--Intermediate-orange">
</p>

<p align="center">
  A Python-based image processing project that converts a color image (RGB) into a grayscale image using manual numerical computation and array operations. (Time taken: 1–2 days)
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Load image dynamically using file dialog</li>
  <li>Manual RGB → Grayscale conversion using weighted formula</li>
  <li>Pixel-level processing using NumPy</li>
  <li>Visualization using Matplotlib</li>
  <li>Optional convolution (blur) using custom kernel</li>
</ul>

<hr>

<h2>How It Works</h2>
<ol>
  <li>Load an image using a file picker</li>
  <li>Convert image into NumPy array</li>
  <li>Extract RGB channels</li>
  <li>Apply grayscale formula:</li>
</ol>

<pre>
Grayscale = 0.299 * R + 0.587 * G + 0.114 * B
</pre>

<ol start="5">
  <li>Display and save grayscale output</li>
  <li>(Optional) Apply convolution for blur effect</li>
</ol>

<hr>

<h2>Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>NumPy (array operations)</li>
  <li>PIL (image loading)</li>
  <li>Matplotlib (visualization)</li>
  <li>Tkinter (file dialog)</li>
</ul>

<hr>

<h2>How to Run</h2>

<pre>
python grayscale_converter.py
</pre>

<ul>
  <li>Select an image file when prompted</li>
  <li>View original and grayscale outputs</li>
</ul>

<hr>

<h2>Future Improvements</h2>
<ul>
  <li>Implement optimized convolution (vectorized / FFT)</li>
  <li>Add multiple filters (edge detection, sharpening)</li>
  <li>Build GUI interface</li>
  <li>Batch image processing support</li>
</ul>

<hr>

<h2>Preview</h2>
<p><i>Coming soon: original vs grayscale comparison</i></p>

<hr>

<h2>Project Structure</h2>

<pre>
02_Color-to-Grayscale-Converter/
│── grayscale_converter.py
│── README.md
</pre>

<hr>

<h2>Author</h2>
<p><b>Master-Zero1</b></p>

<p align="center">
  If you find this useful, consider giving it a star! ⭐
</p>

<hr>

</body>
</html>