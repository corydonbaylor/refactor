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
