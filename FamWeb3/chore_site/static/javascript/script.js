//js nav bar on scroll
window.addEventListener('scroll', function(){
  const header = document.querySelector('header');
  header.classList.toggle('sticky', window.scrollY > 0)
});

//javascript of responsive navigation siderbar menu

const menuBtn = document.querySelector(".menu-btn");
const navigation = document.querySelector(".navigation");
const navigationItems = document.querySelectorAll('.navigation a')


menuBtn.addEventListener("click", () => {
  menuBtn.classList.toggle("active");
  navigation.classList.toggle("active");
});

navigationItems.forEach((navigationItem) => {
  navigationItem.addEventListener("click", () => {
    menuBtn.classList.remove("active");
    navigation.classList.remove("active");
  })
})

//javascript for scrollToTop
const scrollBtn = document.querySelector('.scrollToTop-btn');

window.addEventListener('scroll', function(){
  scrollBtn.classList.toggle('active', window.scrollY > 500)
})

//javascript for scroll back to scrollToTop
scrollBtn.addEventListener('click', () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
})