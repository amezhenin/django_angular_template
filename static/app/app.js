'use strict';

angular.module('XYZ', [
  'XYZ.login',
  'XYZ.dashboard',
  'XYZ.navbar',
  'XYZ.authService'
  //'XYZ.constants'
])
  .config(['$urlRouterProvider', '$locationProvider', '$httpProvider',
    function ($urlRouterProvider, $locationProvider, $httpProvider) {
      $urlRouterProvider.otherwise('/login');

      $locationProvider.html5Mode({
        enabled: true,
        requireBase: true
      });

      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

      // turn on $log.debug, when we are in local/dev environment
      // $logProvider.debugEnabled(DEV_SERVER);
    }]);