var dhi = dhi || {};
dhi.efc = dhi.efc || {};
dhi.efc.newssearch = (function() {
    'use strict';

    var form = $('#news-article-search-form');

    function makeQueryRequest() {
        var path = form.attr('action');
        var query = form.find('#newsarticle-search-text');
        if (!query || !query.val().trim()) {
            return;
        }
        var sanitizedQuery = query.val().trim().replace(/[!'()*-._~<>^]/g, '');

        var qs = "?query=" + encodeURIComponent(sanitizedQuery);
        var requestURL = path + qs;
        window.location.href = requestURL;
    }

    function init() {
        form.on('submit', function (e) {
            e.preventDefault();
            makeQueryRequest();
        });
    }

    return {
        setupSubscribeHandler: init
    };
}());
