const container = document.getElementById('grid-container');
if (!container) {
    console.error('Grid container not found!');
}

const items = [
    { size: '2x2', image: 'static/images/finals/barchart_race.gif' },
    { size: '1x1', image: 'static/images/finals/calendar.png' },
    { size: '1x1', image: 'static/images/finals/covid19_dot_map.gif' },
    { size: '1x2', image: 'static/images/finals/grammys.png' },
    { size: '2x1', image: 'static/images/finals/joy_plot.png' },
    { size: '2x2', image: 'static/images/finals/p5_final.png' },
    { size: '1x1', image: 'static/images/finals/rock.png' },
    // Add more items as needed
];

function createGrid() {
    console.log('Creating grid...');
    container.innerHTML = '';
    items.forEach((item, index) => {
        console.log(`Creating item ${index + 1}...`);
        const div = document.createElement('div');
        div.className = `grid-item item-${item.size}`;
        
        const img = document.createElement('img');
        img.src = item.image;
        img.alt = `Image ${index + 1}`;
        img.onerror = () => console.error(`Failed to load image: ${item.image}`);
        
        div.appendChild(img);
        container.appendChild(div);
        console.log(`Item ${index + 1} added to grid`);
    });
    
    console.log(`Grid created with ${container.children.length} items`);
}

document.addEventListener('DOMContentLoaded', createGrid);
