// Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Import the CSS file

function Header() {
    return (
        <header className="header">
            <h1 className="header-title">Starlight Tracker</h1>
            <div className="scroll-container"> {/* Scrollable container */}
                <nav className="nav">
                    <Link className="nav-link" to="/">Home</Link>
                    <Link className="nav-link" to="/star-info">Star Info</Link>
                    <Link className="nav-link" to="/constellation-info">Constellation Info</Link>
                    
                    <Link className="nav-link" to="/space-news">Latest Space News</Link>
                    <Link className="nav-link" to="/feedback">Feedback</Link>
                    


        
                    <Link className="nav-link" to="/planetary-info">Planetary Info</Link>
                    <Link className="nav-link" to="/astronomy-events">Astronomy Events</Link>
                    <Link className="nav-link" to="/space-facts">Space Facts</Link>
                    <div style={{ position: 'absolute', top: '10px', right: '100px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
    <Link className="nav-link" to="/login" style={{ padding: '10px', textAlign: 'center' }}>Login</Link>
    <Link className="nav-link" to="/signup" style={{ padding: '10px', textAlign: 'center' }}>Signup</Link>
</div>

                    
                </nav>
            </div>
        </header>
    );
}

export default Header;
