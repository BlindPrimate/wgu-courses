/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./apps/course_selector/static/js/app.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./apps/course_selector/static/js/app.js":
/*!***********************************************!*\
  !*** ./apps/course_selector/static/js/app.js ***!
  \***********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

const course_card_links = Object.values(document.querySelectorAll('[data-card-index-link]'));
const possible_click_targets = course_card_links.map(link => {
  return link.dataset.cardIndexLink;
}); // helper function to show set of elements

const show_elements = elements => {
  if (!NodeList.prototype.isPrototypeOf(elements)) {
    elements.classList.remove('hidden');
  } else {
    elements.forEach(element => {
      element.classList.remove('hidden');
    });
  }
}; // helper function to hide set of elements


const hide_elements = elements => {
  if (!NodeList.prototype.isPrototypeOf(elements)) {
    elements.classList.add('hidden');
  } else {
    elements.forEach(element => {
      element.classList.add('hidden');
    });
  }
}; // Apply 'active' class to currently selected card link


const change_link_state = target_card => {
  course_card_links.forEach(e => e.classList.remove("active"));
  target_card.classList.add('active');
}; // swap visible cards


const switch_card = card_id => {
  const all_cards = document.querySelectorAll('[data-card-index');
  const target_card = document.querySelector(`[data-card-index='${card_id}']`);
  const target_link = document.querySelector(`[data-card-index-link='${card_id}']`);
  change_link_state(target_link);
  hide_elements(all_cards);
  show_elements(target_card);
};

(() => {
  // event listener for card-switcher (coures & degrees page)
  window.addEventListener('mousedown', x => {
    const click_target = x.target.dataset.cardIndexLink;

    if (possible_click_targets.includes(click_target)) {
      switch_card(click_target);
    }
  }); // prevent card-switching code from firing on anything other than card links

  const path = window.location.pathname.split('/');
  const course_target_id = path[path.length - 2]; // handles external links to load specific course-card by id
  // www.domain.com/courses/<id>

  if (possible_click_targets.includes(course_target_id)) {
    switch_card(course_target_id);
  } else {
    switch_card(possible_click_targets[0]);
  }
})();

/***/ })

/******/ });
//# sourceMappingURL=app.bundle.js.map