/* toggle_visibility --- Client side WebUI toggles
 *
 * Add selectors as they annoy you.
 *
 *   A small button `[+]' spawns in the right bottom corner to toggle
 * elements of the `toggleable' list; elements in `blacklist' won't
 * come back until you reload the website. Elements in blacklist are
 * to be merged to permanent stylesheet once tested not to break
 * functionality. Call the script again and the button will disappear.
 * if you don't want the button, just remove it from the script.
 *
 */

(() => {
    // Hide select elements
    function hideElements(selectors) {
        selectors.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(element => {
                element.style.display = "none";
            });
        });
    }

    // Toggle visibility of select elements
    function toggleVisibility(selectors) {
        selectors.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(element => {
                if (!element.dataset.originalDisplay) {
                    const computedStyle = getComputedStyle(element);
                    element.dataset.originalDisplay = computedStyle.display === "none" ? "" : computedStyle.display;
                }
                element.style.display = (element.style.display === "none")
                    ? element.dataset.originalDisplay
                    : "none";
            });
        });
    }

    let highestZ = Math.max(
        1,
        ...Array.from(document.querySelectorAll(".draggable"))
            .map(e => parseInt(getComputedStyle(e).zIndex) || 0)
    );

    function bringToFront(el) {
        highestZ += 1;
        el.style.zIndex = highestZ;
    }

    // Make select elements draggable
    function makeDraggable(selectors) {
        selectors.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(element => {
                element.style.position = "absolute";
                element.style.cursor = "grab";
                element.classList.add("draggable");

                let offsetX = 0, offsetY = 0, isDragging = false;

                element.addEventListener("mousedown", e => {
                    isDragging = true;
                    bringToFront(element);
                    element.style.cursor = "grabbing";
                    offsetX = e.clientX - element.offsetLeft;
                    offsetY = e.clientY - element.offsetTop;
                    document.body.style.userSelect = "none";
                });

                document.addEventListener("mousemove", e => {
                    if (!isDragging) return;
                    element.classList.add("dragging");
                    element.style.left = (e.clientX - offsetX) + "px";
                    element.style.top = (e.clientY - offsetY) + "px";
                });

                document.addEventListener("mouseup", () => {
                    isDragging = false;
                    element.style.cursor = "grab";
                    element.classList.remove("dragging");
                    document.body.style.userSelect = "";
                });
            });
        });
    }

    function exemptImage(el) {
        ["dragover", "drop", "mousedown", "pointerdown", "focus"].forEach(type => {
            el.addEventListener(type, function (e) {
                e.stopPropagation();
                e.preventDefault();
            }, { passive: false });
        });
    }

    document.querySelectorAll("img.img").forEach(exemptImage);

    const observer = new MutationObserver(muts => {
        muts.forEach(m => {
            m.addedNodes.forEach(node => {
                if (node.nodeType === 1 && node.matches("img.img")) {
                    exemptImage(node);
                }
            });
        });
    });
    observer.observe(document.body, { childList: true, subtree: true });

    const draggables = [
        "#vector-page-titlebar-toc",
        ".toggleButton",
        ".vector-dropdown.vector-main-menu-dropdown",
        "div.msg-parts-container",
        ".canvas-avatar",
        "div#thread-bottom-container",
        "#vector-page-titlebar-toc-label",      /* Wikipedia TOC sticky widget */
        "#archnavbar",                          /* archwiki */
        "mws-message-compose",
    ];

    const blacklist = [
        "::-webkit-scrollbar",
        "::-webkit-scrollbar-thumb",
        "::-webkit-scrollbar-track",
        "#WIX_ADS",
        ".block.z-21",
        "#truste-consent-track",      /* RedHat Cookie Consent */
        " div.fEy1Z2XT ",
        ".YtwTopBannerImageTextIconButtonedLayoutViewModelHost",
        ".YtwAdImageViewModelHostImage",
        ".YtwSquareImageViewModelHostImage",
        ".YtwAdImageViewModelHostContainer",
        ".ytp-ad-persistent-progress-bar",
        ".ytp-ad-progress",
        ".ytp-ad-progress-list",
        ".ytd-in-feed-ad-layout-renderer",
        ".ytd-in-feed-ad-slot-renderer",
        ".ytd-watch-next-secondary-results-renderer",
        ".yt-core-image",
        ".frb-nag-link",
        ".RPL9esU9f8nMDBntEfZQ",
        ".a2a_kit",
        ".a2a.a2a_kit_size_36.a2a_floating_style.a2a_default_style",
        ".OINTechPromoRightBarBanner",
        ".widget",
        "#ghost-portal-root",                 /* FOSS membership overlay */
        ".ot-sdk-row",
        "#launcher",                          /* Discogs Chat Button */
        ".ad_container",                      /* discogs overlay crap */
        ".ad_bottom",
        ".ot-floating-button",
        ".sc-1w3tvxe-0",
        "#ot-sdk-btn-floating",
        ".sc-1q9fwvy-0",
        ".cookie-notifications",               /* Cookie notifications */
        ".cookie-bar",
        ".glue-cookie-notification-bar",
        "#sliding-popup",
        ".gnav.CookiePrivacyNoticeBanner",
        ".gHHEeh",
        ".sc-1k07fow-1",
        ".cbnSms",
        ".wvqEb",
        "#CookiePrivacyNotice",
        "#owaadbar1",
        ".StyledButton-sc-qe3ace-0",
        ".drift-widget-controller.drift-widget-controller--align-right.square.drift-widget-controller--custom-icon.drift-widget-controller--avatar",
        ".drift-widget-message-preview-wrapper",
        ".drift-widget-controller-icon.square",
        ".draggable.sticky.top-0",               /* ChatGPT limitcap popup */
        ".draggable.no-draggable-children.sticky.top-0",
        "#nav-ad",
        "#onetrust-banner-sdk",                  /* SuperUser Cookie Banner */
        "#onetrust-consent-sdk",
        ".cc-window",                            /* Dell Cookie Consent */
        ".spr-lc-light",                         /* Dell Floating Chat */
        ".CookiePrivacyNotice",
        ".td-header-wrap",
        ".td-scroll-up",
        ".scroll-up-visible",
        ".TccjmKV6RraCaCw5L9gd",                 /* ddg feedback-prompt */
        ".c-avStickyVideo",
        ".brz_msg_wall_body",                    /* LaPresse */
    ];

    const toggleable = [
        "#secondary-nav-component",             /* RedHatSecondary Nav */
        "#partial-discussion-sidebar",
        ".OverviewRepoFiles-module__Box_3--Bi2jM",
        ".Layout-sidebar",
        ".gh-header-shadow",                   /* Github */
        ".ecombw",
        ".js-sticky",
        "span .flex",                           /* GPT prompts */
        ".no-draggable",
        "#page-header",
        ".header",
        ".relative w-full",
        ".md\\:pt-0",
        ".flex.w-full.items-start",
        ".draggable",
        ".draggable.sticky.top-0",
        ".cursor-pointer.absolute.z-10",
        ".header-main__slider",                  /* GeeksForGeeks */
        ".header-main",
        "#header-main__slider-outer-div",
        ".top-banner.fallback",	                 /* MDNs Headers */
        ".sticky-header-container",
        "ytd-masthead",
        ".style-scope.ytd-masthead",
        ".site-header",
        ".fixed.inset-x-0",
        "#bmc-wbtn",
        "#top-scroller",
        "#the-top",
        "#menu-blur",
        "#secondary",
        "#below",
        "#background",
        "#pagetop",
        "#top",
        "#header",
        "#subtopnav",
        "#right",
        "#spacemyfooter",
        "#sidebar",
        ".footer",
        ".header",
        "#left-sidebar",
        "#mw-panel",
        "#mw-head",
        "#masthead",
        "#stage-sidebar-tiny-bar",
        ".border-token-border-light",
        ".text-token-secondary",
        ".navbar",
        "footer",
        "header",
        "#dropdown-nav-outer-wrapper",             /* W3School */
        "#dropdown-nav-inner-wrapper",
        "#googleSearch",
        "#top-nav-bar",
        ".topnavcontainer",
        ".topnavbackground",
        ".bg-main.border-b-border.sticky.top-0",  /* DeepWiki */
        ".pointer-events-none.fixed.bottom-2",
        ".s-top-bar",
        ".top-bar-container",                     /* GitLab */
        ".l.m.n.o.c",                             /* medium */
        ".p.q.r.s.t.u.v.w.x.i.d.y.z",
        ".p.q.r.ab.ac",
        ".bh.ww.ab.c.q.ic.wx.lq.wy",
        ".bg-\\[\\#2c9d30\\].z-\\[11\\].text-sm.max-lg\\:sticky.top-0.text-white.flex.items-center.h-\\(--nav-1-height\\).\\[\\&_a\\]\\:hover\\:underline",  /* tutorialpoint */
        ".h-\\(--nav-2-height\\).z-\\[11\\].sticky.bg-white.top-\\(--nav-1-height\\).lg\\:top-0.px-3.flex.items-center.border-b.border-gray-300",
        ".social-share-sticky-menu__wrapper",     /* NetworkWorld */
        ".branded-header",                        /* gglMsg */
        "mws-header.header",
        "mws-message-compose.ng-tns-c3392202998-1.ng-star-inserted",
        "mws-conversations-list",
        "mws-main-nav.main-nav",
        "div[role=\"navigation\"]",
        "div.xfpmyvw.x1u998qt.x1vjfegm",
        "div.compose-container",
    ];

    hideElements(blacklist);
    toggleVisibility(toggleable);
    makeDraggable(draggables);

    let toggleButton = document.querySelector(".toggleButton");
    if (toggleButton === null) {
        toggleButton = document.createElement("button");
        toggleButton.innerText = "+";
        toggleButton.className = "toggleButton";
        toggleButton.style.position = "fixed";
        toggleButton.style.bottom = "60px";
        toggleButton.style.right = "30px";
        toggleButton.style.zIndex = "9999";
        toggleButton.style.paddingRight = "10px";
        toggleButton.classList.add("liquid-glass", "rounded-full", "items-center", "justify-center", "bg-clip-padding");
        toggleButton.style.backgroundColor = "rgba(0, 0, 0, 0.25)";
        toggleButton.style.backdropFilter = "blur(3px)";
        toggleButton.style.fontSize = "24px";
        toggleButton.style.width = "2rem";
        toggleButton.style.height = "2rem";
        toggleButton.style.color = "rgba(255, 255, 255, 0.0)";
        toggleButton.style.cursor = "pointer";

        toggleButton.addEventListener("click", () => {
            toggleVisibility(toggleable);
            if (toggleButton.innerText == "+") {
                toggleButton.innerText = "";
            } else {
                toggleButton.innerText = "+";
            }
        });
        document.body.appendChild(toggleButton);
    } else {
        toggleButton.remove();
    }

    let isDragging = false;
    let offsetX, offsetY;

    toggleButton.addEventListener('mousedown', (e) => {
        isDragging = true;
        toggleButton.style.cursor = "grabbing";
        offsetX = e.clientX - toggleButton.getBoundingClientRect().left;
        offsetY = e.clientY - toggleButton.getBoundingClientRect().top;
        e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            toggleButton.style.left = `${e.clientX - offsetX}px`;
            toggleButton.style.top = `${e.clientY - offsetY}px`;
            toggleButton.style.bottom = 'auto';
            toggleButton.style.right = 'auto';
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
        toggleButton.style.cursor = "pointer";
    });
})();
