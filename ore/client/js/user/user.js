angular.module('ore.user')
    .value('anonymousUser', {anonymous: true})
    .factory('User', function (anonymousUser) {

        var current = anonymousUser;

        return {
            login: function (username, password) {

            },
            logout: function () {

            },
            isAnoynmous: function () {
                return !!current.anonymous;
            },
            current: function () {
                return current;
            }
        }

    });
