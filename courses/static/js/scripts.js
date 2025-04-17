// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    const courseTypeSelect = document.getElementById('course-type-select');
    const courseList = document.getElementById('course-list');
    
    // Update courses based on selected type
    courseTypeSelect.addEventListener('change', function () {
        const selectedType = this.value;
        
        // Make a fetch request to the server based on the selected course type
        fetch(`/courses/?course_type=${selectedType}`)
            .then(response => response.json())
            .then(data => {
                courseList.innerHTML = '';
                
                data.courses.forEach(course => {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `<a href="${course.url}">${course.title}</a> - ${course.is_online ? 'Онлайн' : 'Оффлайн'}`;
                    courseList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error:', error));
    });
});
