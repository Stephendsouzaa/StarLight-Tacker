import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Home() {
    const [stars, setStars] = useState([]);

    useEffect(() => {
        const fetchStars = async () => {
            try {
                const response = await axios.get('/api/stars');
                setStars(response.data);
            } catch (err) {
                console.error("Error fetching stars:", err);
            }
        };
        fetchStars();
    }, []);

    return (
        <div>
            <h2>Welcome to Starlight Tracker</h2>
            <h3>Famous Stars</h3>
            <ul>
                {stars.map(star => (
                    <li key={star.id}>{star.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default Home;
