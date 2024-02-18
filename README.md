<!DOCTYPE html>
<html lang="cn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>基于扩散模型(Difffusion model)的图片生成</h1>

  <p>本项目是一个基于扩散模型的图片生成项目，可以根据用户输入的文本描述或草图生成高质量图片。可以部署到本地，也可以直接运行在云平台上，如Google Colab</p>

  <h3>快速使用，直接跑在Google Colab上</h3>

  <ol>
    <li>打开 Google Colab 并打开项目中的 <code>demo.ipynb</code> 文件。</li>
    <li>第一个cell中的代码会下载本项目的文件以及该模型所需的开源参数，相当于在colab中复制一份该repo</li>
    <li>按需修改 <code>prompt</code> 内容，即您希望生成的图片的文本描述或草图。</li>
    <li>可以通过是否注释掉代码<code># input_image = Image.open(image_path)</code>进而控制是否在已有的图片上进行魔改</li>
    <li>运行代码。</li>
    
  </ol>

  <h3>示例</h3>
  

  <p>以下是一个示例：</p>

  <p><strong>prompt:</strong> A beautiful stary sky.</p>

  <p><img src="https://github.com/DeepCooder/Image-generation-based-on-stable-diffusion/blob/main/images/generated.jpg" alt="sky"></p>

  <h3>其他说明</h3>

  <ul>
    <li>您可以修改代码中的参数来调整生成的图片质量和风格。</li>
    <li>如果你要部署在自己的电脑上，请手动下载以下文件，并保存在<code>data</code>文件夹中。</li>
    <ul>
      <li>从 https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main 下载 v1-5-pruned-emaonly.ckpt 并将其保存在<code>data</code>文件夹中</li>
      <li>从 https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main/tokenizer 下载 vocab.json 和 merges.txt 并将它们保存在<code>data</code>文件夹中</li>
    </ul>
  </ul>
  <h3>感谢</h3>
  <li>https://www.youtube.com/@umarjamilai</li>
<br>

  <p>希望您能使用本项目生成自己喜欢的图片🖌！</p>
</body>
</html>

<!-- 分割线 -->

<!DOCTYPE html>

<html lang="en">

<head>

 <meta charset="UTF-8">

 <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body>

 <h1>Image generation based on diffusion model</h1>
 
 <p>This project is an image generation project based on diffusion model. It can generate high-quality images according to the text description or sketch input by users. It can be deployed locally or run directly on cloud platforms like Google Colab.</p>

 <h3>Quick start on Google Colab</h3>

 <ol>
  
  <li>Open Google Colab and open the <code>demo.ipynb</code> file in the project.</li>
  
  <li>The code in the first cell will download the files of this project and the open source parameters required by the model, which is equivalent to copying this repo in colab.</li>

  <li>Modify the <code>prompt</code> content as needed, which is the text description or sketch of the image you want to generate.</li>

  <li>You can control whether to modify the existing image by commenting out the code <code># input_image = Image.open(image_path)</code>.</li>

  <li>Run the code.</li>

 </ol>

 <h3>Example</h3>

 <p>Here is an example:</p>

 <p><strong>Prompt:</strong> A beautiful stary sky.</p>

 <p><img src="https://github.com/DeepCooder/Image-generation-based-on-stable-diffusion/blob/main/images/generated.jpg" alt="sky"></p>

 <h3>Other notes</h3>

 <ul>

  <li>You can modify the parameters in the code to adjust the quality and style of the generated images.</li>
  <li>If you want to deploy on your own computer, please manually download the following files and save them in the <code>data</code> folder.</li> <ul> <li>Download v1-5-pruned-emaonly.ckpt from https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main and save it in the <code>data</code> folder</li> <li>Download vocab.json and merges.txt from https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main/tokenizer and save them in the <code>data</code> folder</li> </ul>

 </ul>

 <p>Hope you can generate images you like with this project!</p>

</body>

</html>
