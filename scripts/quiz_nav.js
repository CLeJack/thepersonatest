
document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll('.quiz-content');
    const nextButtons = document.querySelectorAll('.next');
    var current = 0;

    nextButtons.forEach((btn) => {
        btn.addEventListener('click', () => {
        questions[current].classList.remove('active');
        current = Math.min(current + 1, questions.length - 1);
        questions[current].classList.add('active');
        console.log("pressed");
        });
    });
});

