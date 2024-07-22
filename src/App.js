// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
    const [audioFile, setAudioFile] = useState(null);
    const [transcript, setTranscript] = useState('');
    const [isProcessing, setIsProcessing] = useState(false);
    const [error, setError] = useState('');

    const handleFileChange = (event) => {
        setAudioFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (!audioFile) return;
        setIsProcessing(true);
        setError('');

        try {
            const formData = new FormData();
            formData.append('file', audioFile);

            
            const sttResponse = await axios.post('http://localhost:5000/stt', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            setTranscript(sttResponse.data.transcript);

          
            const llmResponse = await axios.post('http://localhost:5000/llm', { text: sttResponse.data.transcript });
            
           
            const ttsResponse = await axios.post('http://localhost:5000/tts', { text: llmResponse.data.text });
            
            
            console.log('TTS Response:', ttsResponse.data);

        } catch (err) {
            setError("good evening being ladies and gentlemen we like to welcome you to flu down your radio broadcast of the" );
        } finally {
            setIsProcessing(false);
        }
    };

    return (
        <div className="App">
            <h1>Voice Bot</h1>
            <input type="file" accept="audio/*" onChange={handleFileChange} />
            <button onClick={handleUpload} disabled={isProcessing}>
                {isProcessing ? 'Processing...' : 'Upload and Process'}
            </button>
            {transcript && <p>Transcript: {transcript}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default App;
