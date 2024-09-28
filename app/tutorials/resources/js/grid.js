// script.js

// Select all grid items
const gridItems = document.querySelectorAll('.grid-item');

// Add click event listener to each grid item
gridItems.forEach(item => {
    item.addEventListener('click', () => {
        // Get the index of the clicked item
        const index = Array.from(gridItems).indexOf(item);
        
        // Check if the clicked item is an even-numbered box (Box 2, Box 4, etc.)
        if ((index + 1) % 2 === 0) { // +1 because index is zero-based
            // Get the previous box (odd-numbered)
            const previousItem = gridItems[index - 1];

            // Swap classes
            const currentOrderClass = item.classList[1]; // Get current order class (e.g., order-2)
            const previousOrderClass = previousItem.classList[1]; // Get previous order class (e.g., order-1)

            // Apply new classes
            item.classList.remove(currentOrderClass);
            item.classList.add(previousOrderClass);

            previousItem.classList.remove(previousOrderClass);
            previousItem.classList.add(currentOrderClass);
        }
        
        // Optionally expand or collapse boxes here if needed
        item.classList.toggle('expanded'); // Example toggle for expansion
    });
});

// Select all grid items

// Add click event listener to each grid item
gridItems.forEach(item => {
    item.addEventListener('click', () => {
        // Find the word list within this grid item
        const wordList = item.querySelector('.word-list');
        
        if (wordList) {
            // Toggle the visibility of the word list
            if (wordList.style.display === 'none' || wordList.style.display === '') {
                wordList.style.display = 'block';
                item.classList.add('expanded');
            } else {
                wordList.style.display = 'none';
                item.classList.remove('expanded');
            }
        }
        
        // Optional: Close other open lists
        gridItems.forEach(otherItem => {
            if (otherItem !== item) {
                const otherWordList = otherItem.querySelector('.word-list');
                if (otherWordList) {
                    otherWordList.style.display = 'none';
                }
                otherItem.classList.remove('expanded');
            }
        });
    });
});


