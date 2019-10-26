const course_card_links = Object.values(document.querySelectorAll('[data-card-index-link]'));
const possible_click_targets = course_card_links.map((link) => {
    return link.dataset.cardIndexLink;
});


// helper function to show set of elements
const show_elements = (elements) => {
    if(!NodeList.prototype.isPrototypeOf(elements)) {
        elements.classList.remove('hidden');
    } else {
        elements.forEach((element) => {
            element.classList.remove('hidden');
        });
    }
}


// helper function to hide set of elements
const hide_elements = (elements) => {
    if(!NodeList.prototype.isPrototypeOf(elements)) {
        elements.classList.add('hidden');
    } else {
        elements.forEach((element) => {
            element.classList.add('hidden');
        });
    }
}

// Apply 'active' class to currently selected card link
const change_link_state = (target_card) => {
    course_card_links.forEach((e) => e.classList.remove("active"));
    target_card.classList.add('active');
}

// swap visible cards
const switch_card = (card_id) => {
    const all_cards = document.querySelectorAll('[data-card-index');
    const target_card = document.querySelector(`[data-card-index='${card_id}']`)
    const target_link = document.querySelector(`[data-card-index-link='${card_id}']`)
    change_link_state(target_link);
    hide_elements(all_cards);
    show_elements(target_card);
}

(() => {

    // event listener for card-switcher (coures & degrees page)
    window.addEventListener('mousedown', (x) => {
        const click_target = x.target.dataset.cardIndexLink;
        if (possible_click_targets.includes(click_target)) {
            switch_card(click_target);
        }
    });


    // prevent card-switching code from firing on anything other than card links
    const path = window.location.pathname.split('/');
    const course_target_id = path[path.length - 2];

    // handles external links to load specific course-card by id
    // www.domain.com/courses/<id>
    if (possible_click_targets.includes(course_target_id)) {
        switch_card(course_target_id);
    } else {
        switch_card(possible_click_targets[0])
    }



})();