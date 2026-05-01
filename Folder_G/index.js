const { exec } = 
require('child_process'); 
const path = require('path'); 
const CONFIG = {
    foto: 'member.jpg', 
    audio: 'backsound.mp3', 
    output: 
    'konten_member_global.mp4', 
    durasi: 60, resolusi: 
    '1080:1920'
};
const perintah = `ffmpeg 
-loop 1 -i ${CONFIG.foto} -i 
${CONFIG.audio} \ -c:v 
libx264 -t ${CONFIG.durasi} 
-pix_fmt yuv420p \ -vf 
"scale=${CONFIG.resolusi}:force_original_aspect_ratio=increase,crop=${CONFIG.resolusi}" 
\ -c:a aac -shortest 
${CONFIG.output} -y`; 
console.log("--------------------------------------------------"); 
console.log("PIRAMIDA GUARD - 
VIDEO ENGINE v1.0"); 
console.log("Sedang memproses 
konten Indramayu Club..."); 
console.log("--------------------------------------------------"); 
exec(perintah, (error, 
stdout, stderr) => {
    if (error) { 
        console.error(`[ERROR]: 
        ${error.message}`); 
        return;
    }
    console.log(`[SUCCESS]: 
    Video Berhasil Dibuat -> 
    ${CONFIG.output}`);
});
