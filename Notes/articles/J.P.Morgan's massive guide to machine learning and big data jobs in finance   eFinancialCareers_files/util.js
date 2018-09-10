var dhi = dhi || {};
dhi.efc = dhi.efc || {};
dhi.efc.util = (function() {
    'use strict';

    function isLocalhost() {
        return location.port === '8080';
    }

    function getCookie(name) {
        var regexp = new RegExp(name + '=([\\w-,]+);?'),
            matches = document.cookie.match(regexp);
        if (!matches || !matches[1]) {
            return null;
        }
        return matches[1];
    }

    function setCookie(name, value) {
        var date = new Date(),
            year = date.getFullYear(),
            path = '/',
            cookie;
        date.setFullYear(year + 2);
        if (isLocalhost()) {
            path += 'site';
        }
        cookie = name + '=' + value + '; expires=' + date.toGMTString() + '; path=' + path;
        console.debug('Setting cookie ' + cookie);
        document.cookie = cookie;
    }

    return {
        isLocalhost: isLocalhost,
        getCookie: getCookie,
        setCookie: setCookie
    };
}());
