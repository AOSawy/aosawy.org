/* scroll-behavior.js — Site-wide UX enhancements
   1. Tab persistence  2. Scroll persistence  3. Scroll-to-content on tab click
   4. Scroll-to-top button  5. Back-to-Portfolio breadcrumb
   6. Skip-to-content link  7. Keyboard arrow tabs  8. Reading progress
   9. Image lightbox  10. Story navigation */

(function() {
  var key = 'scrollY_' + location.pathname;
  var tabKey = 'activeTab_' + location.pathname;
  var navType = (performance.getEntriesByType('navigation')[0] || {}).type;
  var isReload = navType === 'reload';
  var restoringTab = false;
  var userClicked = false;

  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';

  var savedTab = sessionStorage.getItem(tabKey);
  var savedScroll = isReload ? sessionStorage.getItem(key) : null;
  if (!isReload) sessionStorage.removeItem(key);

  // === TAB RESTORE ===
  if (savedTab) {
    var attempts = 0;
    function tryRestore() {
      if (userClicked || attempts > 30) return;
      attempts++;
      var allButtons = document.querySelectorAll('button');
      for (var i = 0; i < allButtons.length; i++) {
        if (allButtons[i].textContent.trim() !== savedTab) continue;
        var parent = allButtons[i].parentElement;
        if (!parent || parent.querySelectorAll('button').length < 3) continue;
        restoringTab = true;
        allButtons[i].click();
        restoringTab = false;
        return;
      }
      setTimeout(tryRestore, 500);
    }
    setTimeout(tryRestore, 2000);
  } else if (savedScroll) {
    var scrollTarget = parseInt(savedScroll, 10);
    var scrollDone = false;
    function tryScroll() {
      if (scrollDone) return;
      if (document.documentElement.scrollHeight >= scrollTarget + 100) {
        scrollDone = true;
        window.scrollTo(0, scrollTarget);
      } else {
        requestAnimationFrame(tryScroll);
      }
    }
    requestAnimationFrame(tryScroll);
  }

  window.addEventListener('beforeunload', function() {
    sessionStorage.setItem(key, window.scrollY);
  });

  // === TAB CLICK HANDLER ===
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('button');
    if (!btn) return;
    var parent = btn.parentElement;
    var isTab = false;
    if (parent && parent.querySelectorAll('button').length >= 3) isTab = true;
    if (!isTab && btn.closest('.sh-nav')) isTab = true;
    if (!isTab && btn.closest('[role="tablist"]')) isTab = true;

    if (isTab) {
      if (!restoringTab) {
        userClicked = true;
        // Find the tab bar and calculate scroll target BEFORE React changes state
        var tabBar = parent || btn.parentElement;
        var siteHeader = document.querySelector('.ds-site-header');
        var headerH = siteHeader ? siteHeader.offsetHeight : 0;
        var tabBarTop = tabBar.getBoundingClientRect().top + window.scrollY;
        var target = Math.max(0, tabBarTop - headerH);
        // Scroll immediately AND after React's hash change / state update
        window.scrollTo({ top: target, behavior: 'smooth' });
        setTimeout(function() { window.scrollTo({ top: target, behavior: 'instant' }); }, 150);
      }
      sessionStorage.setItem(tabKey, btn.textContent.trim());
    }
  });

  // === KEYBOARD ARROW NAVIGATION FOR TABS ===
  document.addEventListener('keydown', function(e) {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    var focused = document.activeElement;
    if (!focused || focused.tagName !== 'BUTTON') return;
    var parent = focused.parentElement;
    if (!parent || parent.querySelectorAll('button').length < 3) return;

    var buttons = Array.from(parent.querySelectorAll('button'));
    var idx = buttons.indexOf(focused);
    if (idx === -1) return;

    e.preventDefault();
    var next = e.key === 'ArrowRight'
      ? buttons[(idx + 1) % buttons.length]
      : buttons[(idx - 1 + buttons.length) % buttons.length];
    next.focus();
    next.click();
  });

  // === INIT FEATURES ON DOM READY ===
  function init() {
    createSkipLink();
    createScrollTopBtn();
    createBreadcrumb();
    createReadingProgress();
    createLightbox();
    createStoryNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // === SKIP-TO-CONTENT LINK ===
  function createSkipLink() {
    var link = document.createElement('a');
    link.className = 'ds-skip-link';
    link.href = '#root';
    link.textContent = 'Skip to content';
    document.body.insertBefore(link, document.body.firstChild);
  }

  // === SCROLL-TO-TOP BUTTON ===
  function createScrollTopBtn() {
    var btn = document.createElement('button');
    btn.className = 'ds-scroll-top';
    btn.setAttribute('aria-label', 'Scroll to top');
    var ns = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    var path = document.createElementNS(ns, 'path');
    path.setAttribute('d', 'M18 15l-6-6-6 6');
    svg.appendChild(path);
    btn.appendChild(svg);
    document.body.appendChild(btn);

    btn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    var visible = false;
    window.addEventListener('scroll', function() {
      var shouldShow = window.scrollY > 600;
      if (shouldShow !== visible) {
        visible = shouldShow;
        btn.classList.toggle('visible', visible);
      }
    }, { passive: true });
  }

  // === BREADCRUMB: BACK TO PORTFOLIO ===
  function createBreadcrumb() {
    if (!document.body.classList.contains('page-showcase')) return;
    var bc = document.createElement('div');
    bc.className = 'ds-breadcrumb';
    var a = document.createElement('a');
    a.href = '/portfolio';
    var ns = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    var p = document.createElementNS(ns, 'path');
    p.setAttribute('d', 'M15 18l-6-6 6-6');
    svg.appendChild(p);
    a.appendChild(svg);
    var span = document.createElement('span');
    span.textContent = 'Portfolio';
    a.appendChild(span);
    bc.appendChild(a);
    document.body.appendChild(bc);

    var visible = false;
    window.addEventListener('scroll', function() {
      var shouldShow = window.scrollY > 400;
      if (shouldShow !== visible) {
        visible = shouldShow;
        bc.classList.toggle('visible', visible);
      }
    }, { passive: true });
  }

  // === READING PROGRESS INDICATOR ===
  function createReadingProgress() {
    var bar = document.createElement('div');
    bar.className = 'ds-reading-progress';
    document.body.appendChild(bar);

    window.addEventListener('scroll', function() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var pct = h > 0 ? (window.scrollY / h) * 100 : 0;
      bar.style.width = pct + '%';
    }, { passive: true });
  }

  // === IMAGE LIGHTBOX ===
  function createLightbox() {
    // Only on showcase pages
    var isShowcase = document.body.classList.contains('page-showcase');
    if (!isShowcase) return;

    var overlay = document.createElement('div');
    overlay.className = 'ds-lightbox';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-label', 'Image viewer');
    var closeBtn = document.createElement('button');
    closeBtn.className = 'ds-lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close image viewer');
    closeBtn.textContent = '\u00d7';
    var img = document.createElement('img');
    img.alt = 'Enlarged view';
    overlay.appendChild(closeBtn);
    overlay.appendChild(img);
    document.body.appendChild(overlay);

    function close() { overlay.classList.remove('open'); }
    closeBtn.addEventListener('click', close);
    overlay.addEventListener('click', function(e) { if (e.target === overlay) close(); });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') close(); });

    // Attach click to content images (wait for React)
    setTimeout(function attachClicks() {
      var main = document.querySelector('main');
      if (!main) { setTimeout(attachClicks, 500); return; }
      main.addEventListener('click', function(e) {
        var target = e.target;
        if (target.tagName !== 'IMG') return;
        // Skip tiny icons/avatars
        if (target.naturalWidth < 100 || target.naturalHeight < 100) return;
        img.src = target.src;
        overlay.classList.add('open');
      });
    }, 2000);
  }

  // === STORY NAVIGATION ===
  function createStoryNav() {
    var storyFlow = [
      { path: '/', label: 'Home' },
      { path: '/research', label: 'Research' },
      { path: '/portfolio', label: 'Portfolio' },
      { path: '/teaching', label: 'Teaching' }
    ];

    var currentPath = location.pathname.replace(/\/$/, '') || '/';
    var idx = -1;
    for (var i = 0; i < storyFlow.length; i++) {
      if (storyFlow[i].path === currentPath) { idx = i; break; }
    }
    // Only show on main story pages
    if (idx === -1) return;

    var prev = idx > 0 ? storyFlow[idx - 1] : null;
    var next = idx < storyFlow.length - 1 ? storyFlow[idx + 1] : null;
    if (!prev && !next) return;

    // Wait for footer to exist, insert before it
    setTimeout(function insertNav() {
      var footer = document.querySelector('.ds-site-footer');
      if (!footer) { setTimeout(insertNav, 500); return; }

      var nav = document.createElement('nav');
      nav.className = 'ds-story-nav';
      nav.setAttribute('aria-label', 'Page navigation');

      if (prev) {
        var a = document.createElement('a');
        a.href = prev.path;
        a.className = 'prev';
        var lbl = document.createElement('span');
        lbl.className = 'label';
        lbl.textContent = '\u2190 Previous';
        var ttl = document.createElement('span');
        ttl.className = 'title';
        ttl.textContent = prev.label;
        a.appendChild(lbl);
        a.appendChild(ttl);
        nav.appendChild(a);
      }
      if (next) {
        var a2 = document.createElement('a');
        a2.href = next.path;
        a2.className = 'next';
        var lbl2 = document.createElement('span');
        lbl2.className = 'label';
        lbl2.textContent = 'Next \u2192';
        var ttl2 = document.createElement('span');
        ttl2.className = 'title';
        ttl2.textContent = next.label;
        a2.appendChild(lbl2);
        a2.appendChild(ttl2);
        nav.appendChild(a2);
      }

      footer.parentNode.insertBefore(nav, footer);
    }, 3000);
  }
})();
