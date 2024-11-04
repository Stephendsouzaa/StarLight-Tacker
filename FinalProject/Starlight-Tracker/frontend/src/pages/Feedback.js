import React, { useState } from 'react';
import axios from 'axios';

function Feedback() {
    const [feedback, setFeedback] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('/api/feedback', { feedback });
        setFeedback('');
        alert('Feedback submitted!');
    };

    return (
        <div>
            <h2>Feedback</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    placeholder="Your feedback here..."
                    required
                />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default Feedback;
