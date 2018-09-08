var dhi = dhi || {};
dhi.efc = dhi.efc || {};
dhi.efc.jobsearch = function() {
    'use strict';

    var form, keywords, keywordsApiKey, keywordsLookup, keywordsSuggest, keywordsVal,
        locId, locName, locSuggest, locData = [], lastRegex = /[^,]*$/, nonLastRegex = /^.+,\s*|/;

    function getLast(input) {
        // example input: 'Account Executive, Account Management, acc'
        // example return: 'acc'
        return input.match(lastRegex)[0].trim();
    }

    function getNonLast(input) {
        // example input: 'Account Executive, Account Management, acc'
        // example return: 'Account Executive, Account Management, '
        return input.match(nonLastRegex)[0];
    }

    function fetchKeywordsData() {
        var query = getLast(keywords.val());
        if (!query || query.length < 3) {
            return;
        }
        if (query == keywordsVal) {
            //text hasn't changed, don't submit another request
            return;
        }
        keywordsVal = query;
        $.ajax({
            url: keywordsLookup + keywordsVal,
            headers: {
                'x-api-key': keywordsApiKey
            }
        }).done(function(json) {
            if (!json.data || !json.data.length || !json.data[0].terms) {
                console.error('no keyword suggestions...');
                keywordsSuggest.list = [];
                return;
            }
            keywordsSuggest.list = json.data[0].terms;
        }).fail(function(jqxhr, textStatus, error) {
            console.error('Fetch keywords failed', textStatus, error);
        });
    }

    function fetchLocationData() {
        if (locData.length) {
            return;
        }
        $.getJSON({
            url: locName.data('lookup'),
            //https://stackoverflow.com/questions/8163703/cross-domain-ajax-doesnt-send-x-requested-with-header
            headers: {'X-Requested-With': 'XMLHttpRequest'}
        }).done(function(json) {
            locData = json;
            locSuggest.list = locData.map(function(l) { return l.displayName; });
        }).fail(function(jqxhr, textStatus, error) {
            console.error('Fetch locations failed', textStatus, error);
        });
    }

    function setLocationId() {
        var val = locName.val();
        for (var i = 0; i < locData.length; i++) {
            if (locData[i].displayName === val) {
                locId.val(locData[i].id);
                return;
            }
        }
        locId.val(0);
    }

    function setupKeywords() {
        keywords = $('#job-search-form-keywords');
        if (!keywords.length) {
            console.error('Missing job search form keywords field');
            return;
        }
        keywordsApiKey = keywords.data('apiKey');
        keywordsLookup = keywords.data('lookup');
        if (!keywordsApiKey || !keywordsLookup) {
            console.error('Missing one or more required data attributes for job search form keywords autocompletion');
            return;
        }
        keywordsSuggest = new Awesomplete(keywords[0], {
            // https://leaverou.github.io/awesomplete/#extensibility
            // https://leaverou.github.io/awesomplete/#multiple-values
            // example initial input value: 'Account Executive, Account Management, acc'
            // example text: 'Account Manager'
            filter: function(text, input) {
                return true;  // else prevents spell corrections, ie Cheif => Chief
            },
            item: function(text, input) {
                // example return: <li aria-selected="false"><mark>Acc</mark>ount Manager</li>
                return Awesomplete.ITEM(text, getLast(input));
            },
            replace: function(text) {
                // example final input value: 'Account Executive, Account Management, Account Manager'
                this.input.value = getNonLast(this.input.value) + text + ', ';
            },
            maxItems: 6,
            minChars: 3
        });
        keywordsVal = keywords.val();
        keywords.on('keyup', fetchKeywordsData);
    }

    function cleanupKeywords(evt) {
        var val = keywords.val();
        val = val.trim().replace(/,$/, '');
        keywords.val(val);
    }

    function setupLocation() {
        locId = $('#job-search-form-location-id');
        locName = $('#job-search-form-location-name');
        if (!locId.length || !locName.length) {
            console.error('Missing job search form location ID and/or name field');
            return;
        }
        locSuggest = new Awesomplete(locName[0], {minChars: 3, maxItems: 6});
        fetchLocationData();
        form.on('submit', setLocationId);
    }

    if (!Awesomplete) {
        console.error('Missing required library');
        return;
    }

    form = $('#job-search-form');

    if (!form.length) {
        console.error('Missing job search form');
        return;
    }

    setupKeywords();
    setupLocation();
    form.on('submit', cleanupKeywords);
}();
