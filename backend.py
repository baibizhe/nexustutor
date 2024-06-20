from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from io import BytesIO
from moviepy.editor import VideoFileClip

app = Flask(__name__)
CORS(app)  # 允许所有域名跨域

# 你可以设置允许上传的文件类型，这里为了简单，默认允许所有类型。
ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'mov', 'flv', 'wmv', 'mkv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload-video', methods=['POST'])
def upload_video():
    # 检查是否有文件在请求中
    # print(17,dir(request))
    print(17,request.files)
 
    # if 'video' not in request.files:
    #     return jsonify({'message': 'No file part'}), 200

    video_file = request.files['video']
    print(19,video_file)
    # # 如果用户未选择文件，浏览器同样提交一个空的表单名，因此要检查文件名是否为空
    # if video_file.filename == '':
    #     return jsonify({'message': 'No selected file'}), 200

    if video_file and allowed_file(video_file.filename):
        # filename = secure_filename(file.filename)
        # 在这里你可以保存文件到文件系统
        # file.save(os.path.join('/path/to/the/uploads', filename))
        video_stream = BytesIO(video_file.stream.read())
        video_clip = VideoFileClip(file_object=video_stream, audio=False)
        
        # Extract audio and convert it into an in-memory bytes stream
        audio_bytes_io = BytesIO()
        video_clip.audio.write_audiofile(audio_bytes_io, codec='mp3')
        audio_bytes_io.seek(0)  # Reset the buffer's position to the beginning
        
        print(f'Received video: {filename}, Size: {len(file.read())} bytes.')

        # 这里我们只打印信息，因为不实际保存文件
        return jsonify({'message': 'Video uploaded successfully!', 'filename': filename}), 200

    # 如果不是我们允许的文件类型
    return jsonify({'message': 'File type not allowed'}), 400

# 启动服务器
if __name__ == '__main__':
    port = 3001
    print(f'Server running on port {port}...')
    app.run(port=port)
