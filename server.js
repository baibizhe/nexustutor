const express = require('express');
const multer = require('multer'); // 用于处理multipart/form-data类型的请求

const app = express();
const cors = require('cors');
app.use(cors()); // 使所有路由都支持跨源请求
const upload = multer(); // 使用默认存储，即不存储文件到磁盘

// 设置上传目录和文件名处理
// const storage = multer.diskStorage({
//   destination: function(req, file, cb) {
//     cb(null, 'uploads/');
//   },
//   filename: function(req, file, cb) {
//     cb(null, Date.now() + '-' + file.originalname);
//   }
// });

// const upload = multer({ storage: storage });
app.post('/upload-video', upload.single('video'), (req, res) => {
    if (req.file) {
        console.log('Received video:', req.file); // 输出文件信息
    }

    // 如果不需要存储视频，你只要伪装后端接受到了视频
    console.log(`Received video. Size: ${req.file.size} bytes.`);

    // 返回成功消息
    res.json({
      success: true,
      message: 'Video uploaded successfully!',
    });
});
// 启动服务器
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
