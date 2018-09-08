$(function() {
    var jobSectorsList, jobSectorsLoading, jobSectorsError;

    function buildJobSectorsList(sectors) {
        if (!sectors) {
            return;
        }
        var ul = $('<ul class="list-unstyled">');
        sectors.forEach(function(sector) {
            var sectorHref = sector.link_url.replace(/^http:/, '');
            ul.append('<li><a href="' + sectorHref + '">' + sector.name + '</a> (' + sector.count + ')</li>');
        });
        jobSectorsList.prepend(ul);
        jobSectorsLoading.hide();
    }

    function fetchJobSectors() {
        $.ajax({
            url: jobSectorsList.data('lookup')
        }).done(function(json) {
            if (!json || !json.top_sectors || !json.top_sectors.length) {
                console.error('Fetch job sectors succeeded but data is missing');
                jobSectorsError.show();
                jobSectorsLoading.hide();
                return;
            }
            buildJobSectorsList(json.top_sectors);
        }).fail(function(jqxhr, textStatus, error) {
            console.error('Fetch job sectors failed', textStatus, error);
            jobSectorsError.show();
            jobSectorsLoading.hide();
        });
    }

    jobSectorsList = $('#job-sectors-list');
    jobSectorsLoading = $('#job-sectors-loading');
    jobSectorsError = $('#job-sectors-error');

    if (!jobSectorsList.length || !jobSectorsLoading.length || !jobSectorsError.length) {
        console.error('Missing job sectors list or something');
        return;
    }

    fetchJobSectors();
});
