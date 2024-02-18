<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>基于扩散模型(Difffusion model)的图片生成</h1>

  <p>本项目是一个基于扩散模型的图片生成项目，可以根据用户输入的文本描述或草图生成高质量图片。可以部署到本地，也可以直接运行在云平台上，如Google Colab</p>

  <h2>快速使用，直接跑在Google Colab上</h2>

  <ol>
    <li>打开 Google Colab 并打开项目中的 <code>demo.ipynb</code> 文件。</li>
    <li>第一个cell中的代码会下载本项目的文件以及该模型所需的开源参数，相当于在colab中复制一份该repo</li>
    <li>按需修改 <code>prompt</code> 内容，即您希望生成的图片的文本描述或草图。</li>
    <li>可以通过是否注释掉代码<code># input_image = Image.open(image_path)</code>进而控制是否在已有的图片上进行魔改</li>
    <li>运行代码。</li>
    
  </ol>

  <h2>示例</h2>

  <p>以下是一个示例：</p>

  <p><strong>prompt:</strong> A beautiful stary sky.</p>

  <p><img src="https://github.com/DeepCooder/Image-generation-based-on-stable-diffusion/blob/main/images/generated.jpg" alt="sky"></p>

  <h2>其他说明</h2>

  <ul>
    <li>您可以修改代码中的参数来调整生成的图片质量和风格。</li>
    <li>项目代码已开源，您可以自由使用和修改。</li>
  </ul>

  <h2>您可以尝试的 prompt</h2>


  <p>希望您能使用本项目生成自己喜欢的图片！</p>
</body>
</html>
