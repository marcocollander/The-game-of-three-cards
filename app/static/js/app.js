const getSelector = (selector) => {
  return document.querySelector(selector);
};

const getSelectors = (selector) => {
  return document.querySelectorAll(selector);
};

function addListener(selector, handler) {
  selector.addEventListener("click", handler);
}

const btns = getSelectors(".btns__btn");

const [btnStart, btnReset] = btns;

const cards = [
  "../static/assets/dama-karo.jpg",
  "../static/assets/dama-pik.jpg",
  "../static/assets/dama-kier.jpg",
];
const card_back = "../static/assets/back.jpg";

const [damaKaro, damaPik, damaKier] = cards;

const images = getSelectors(".wrapper__card");

const [referenceDamaKaro, referenceDamaPik, referenceDamaKier] = images;

let [i, j, k, index, numberOfHits, clickCounter, numberOfAttempts] = [
  0, 1, 2, 0, 0, 0, 0,
];

const hamburger = getSelector(".hamburger");
const hamburgerItems = getSelectors(".hamburger__item");
const menu = getSelector(".menu");


addListener(hamburger, () => {
  menu.classList.toggle("hidden");
  hamburgerItems[0].classList.toggle("rotate-hamburger");
  hamburgerItems[1].classList.toggle("hidden");
  hamburgerItems[2].classList.toggle("reverse-rotate-hamburger");
});

const inputNumberOfAttempts = getSelector("#number_of_attempts");
const inputNumberOfHits = getSelector("#number_of_hits");
const inputPercentageResult = getSelector("#hit_percentage");
const message = getSelector(".hit__message");

btnStart.addEventListener("click", function () {
  clickCounter = 0;
  message.innerHTML = "";
  ++numberOfAttempts;

  inputNumberOfAttempts.value = `${numberOfAttempts}`;
  inputNumberOfHits.value = `${numberOfHits} `;
  inputPercentageResult.value = `${(
    (numberOfHits / numberOfAttempts) *
    100
  ).toFixed(0)}`;

  btnStart.disabled = true;
  btnReset.disabled = false;
  images.forEach((image) => {
    image.classList.toggle("rotate");
    image.classList.toggle("rotate-one");
    image.setAttribute("src", card_back);
  });

  i = Math.floor(Math.random() * 3);
  // const numbers = [0, 1, 2];
  // index = numbers.find((number) => number == i);
  // numbers.splice(index);

  switch (i) {
    case 0:
      (j = 1), (k = 2);
      break;
    case 1:
      (j = 0), (k = 2);
      break;
    case 2:
      (j = 0), (k = 1);
  }
});

btnReset.addEventListener("click", () => {
  let ok = confirm("Czy chcesz zresetować grę?");

  if (ok) {
    btnStart.disabled = false;
    btnReset.disabled = true;
    images.forEach((image, i) => {
      image.setAttribute("src", cards[i]);
      image.classList.toggle("rotate");
      image.classList.toggle("rotate-one");
    });
    clickCounter = 0;
    numberOfAttempts = 0;
    numberOfHits = 0;
    inputNumberOfAttempts.value = 0;
    inputNumberOfHits.value = 0;
    inputPercentageResult.value = 0;
  }
});

referenceDamaKaro.addEventListener("click", () => {
  clickCounter++;
  btnStart.disabled = false;
  if (cards[i] === damaPik && clickCounter === 1) {
    numberOfHits++;
    message.innerHTML = "Hurra, trafiłeś!";
  }
  referenceDamaKaro.setAttribute("src", cards[i]);
  referenceDamaKaro.classList.toggle("rotate");
  referenceDamaKaro.classList.toggle("rotate-one");
});

referenceDamaPik.addEventListener("click", () => {
  clickCounter++;
  btnStart.disabled = false;
  if (cards[j] === damaPik && clickCounter === 1) {
    numberOfHits++;
    message.innerHTML = "Hurra, trafiłeś!";
  }
  referenceDamaPik.setAttribute("src", cards[j]);
  referenceDamaPik.classList.toggle("rotate");
  referenceDamaPik.classList.toggle("rotate-one");
});

referenceDamaKier.addEventListener("click", () => {
  clickCounter++;
  btnStart.disabled = false;
  if (cards[k] === damaPik && clickCounter === 1) {
    numberOfHits++;
    message.innerHTML = "Hurra, trafiłeś!";
  }
  referenceDamaKier.setAttribute("src", cards[k]);
  referenceDamaKier.classList.toggle("rotate");
  referenceDamaKier.classList.toggle("rotate-one");
});
