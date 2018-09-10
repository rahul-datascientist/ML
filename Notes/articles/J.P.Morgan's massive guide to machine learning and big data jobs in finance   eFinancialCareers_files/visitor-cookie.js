(function() {
    var relevanceOrigin;

    function getRelevanceOrigin() {
        if (dhi.efc.util.isLocalhost()) {
            return 'http://localhost:8080';
        }
        return location.origin.substring(0, location.origin.indexOf('efinancialcareers') + 17) + '.com';
    }

    function createIframe(origin) {
        var src = origin,
            iframe;
        if (dhi.efc.util.isLocalhost()) {
            src += '/site/efinancialcareers-us';
        }
        src += '/servlets/visitor-cookie';
        iframe = document.createElement('iframe');
        iframe.src = src;
        iframe.style.display = 'none';
        document.body.appendChild(iframe);
    }

    relevanceOrigin = getRelevanceOrigin();
    if (relevanceOrigin === location.origin) {
        console.debug('Current origin is same as relevance origin - exiting');
        return;
    }
    createIframe(relevanceOrigin);
    window.addEventListener('message', function (event) {
        var cookie;
        console.debug('Received message from ' + event.origin + ' with data ' + event.data);
        if (event.origin !== relevanceOrigin) {
            console.debug('Message origin differs from relevance origin - exiting');
            return;
        }
        cookie = dhi.efc.util.getCookie('_visitor');
        if (cookie === event.data) {
            console.debug('Current _visitor cookie is same as relevance origin - exiting');
            return;
        }
        console.debug('Current _visitor cookie is ' + cookie);
        dhi.efc.util.setCookie('_visitor', event.data);
    });
}());
