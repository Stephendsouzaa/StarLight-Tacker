import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
    const [prompt, setPrompt] = useState('');
    const [response, setResponse] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('/api/chatbot', { prompt });
            setResponse(res.data.response);
        } catch (error) {
            console.error("Error fetching chatbot response:", error);
        }
    };

    return (
        <div className="chatbot">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Ask me something..."
                />
                <button type="submit">Send</button>
            </form>
            {response && <div className="response">{response}</div>}
        </div>
    );
};

export default Chatbot;
