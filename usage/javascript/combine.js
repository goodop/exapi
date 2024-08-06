const path = require('path');
const ExecrossAPI = require('./exapi');
const api = new ExecrossAPI();

async function main() {
    try {
        // # You can empty the files list or urls list if you want use one of them.
        const files = [
            path.resolve(__dirname, '../python/assets/cobrax.jpg'),
            path.resolve(__dirname, '../python/assets/tiger.jpg')
        ];
        const saveImageAs = "utils/combined.jpg"
        const urls = [
            'https://images.nightcafe.studio/jobs/g9k7ET6X4eTnJMIASD9Q/g9k7ET6X4eTnJMIASD9Q--1--83vb5.jpg',
            'https://img.freepik.com/premium-photo/3d-rendering-arabian-cobra-animal-ai-generative_842224-8185.jpg'
        ];
        const result = await api.combineImages(saveImageAs, files, urls);
        if (result.error) {
            console.error('Error:', result.error);
        } else {
            console.log(result.message);
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}

main();
