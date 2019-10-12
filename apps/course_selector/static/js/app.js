const course_card_links = Object.values(document.querySelectorAll('[data-card-index-link]'));
const possible_click_targets = course_card_links.map((link) => {
    return link.dataset.cardIndexLink;
});


const show_elements = (elements) => {
    if(!NodeList.prototype.isPrototypeOf(elements)) {
        elements.classList.remove('hidden');
    } else {
        elements.forEach((element) => {
            element.classList.remove('hidden');
        });
    }
}

const hide_elements = (elements) => {
    if(!NodeList.prototype.isPrototypeOf(elements)) {
        elements.classList.add('hidden');
    } else {
        elements.forEach((element) => {
            element.classList.add('hidden');
        });
    }
}

const switch_card = (card_id) => {
    const all_cards = document.querySelectorAll('[data-card-index');
    const target_card = document.querySelector(`[data-card-index='${card_id}']`)
    hide_elements(all_cards);
    show_elements(target_card);
}

window.addEventListener('mousedown', (x) => {
    const click_target = x.target.dataset.cardIndexLink;
    if (possible_click_targets.includes(click_target)) {
        switch_card(click_target);
    }
});


const path = window.location.pathname.split('/');
const course_target_id = path[path.length - 2];

if (possible_click_targets.includes(course_target_id)) {
    switch_card(course_target_id);
}