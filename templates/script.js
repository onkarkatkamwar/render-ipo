document.addEventListener('DOMContentLoaded', () => {
    const tooltips = document.querySelectorAll('.tooltip');
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseover', () => {
            tooltip.style.backgroundColor = '#45a049';
        });
        tooltip.addEventListener('mouseout', () => {
            tooltip.style.backgroundColor = '#4CAF50';
        });
    });
});
