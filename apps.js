const express = require('express');
const PSD = require('psd');
const fs = require('fs');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Route to parse the PSD file and return its tree structure as JSON
app.get('/psd-tree', async (req, res) => {
    try {
        const psd = PSD.fromFile('/Users/deepakdubey/Downloads/final.psd');
        await psd.parse();

        // Get the tree structure
        const tree = psd.tree().export();

        // Return the tree structure as JSON
        res.json(tree);
    } catch (error) {
        res.status(500).json({ error: 'Failed to parse PSD file', details: error.message });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});