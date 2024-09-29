const container = document.getElementById('grid-container');
if (!container) {
    console.error('Grid container not found!');
}

const items = [
    { size: '2x2', image: 'static/images/finals/barchart_race.gif', title: 'Bar Chart Race', route: 'viz/barchart_race' },
    { size: '1x1', image: 'static/images/finals/calendar.png', title: 'Calendar', route: 'viz/calendar' },
    { size: '1x1', image: 'static/images/finals/covid19_dot_map.gif', title: 'COVID-19 Dot Map', route: 'viz/covid' },
    { size: '1x2', image: 'static/images/finals/grammys.png', title: 'Grammys', route: 'viz/grammys' },
    { size: '2x1', image: 'static/images/finals/joy_plot.png', title: 'Joy Plot', route: 'viz/joyplot' },
    { size: '2x2', image: 'static/images/finals/p5_final.png', title: 'P5 Final', route: 'viz/powerfive' },
    { size: '1x1', image: 'static/images/finals/rock.png', title: 'Rock', route: 'viz/rock' },
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
        img.alt = item.title;
        
        div.appendChild(img);
        container.appendChild(div);

        // Add click event listener
        div.addEventListener('click', () => {
            window.location.href = `/${item.route}`;
        });

        console.log(`Item ${index + 1} added to grid`);
    });
    
    console.log(`Grid created with ${container.children.length} items`);
}

document.addEventListener('DOMContentLoaded', createGrid);
