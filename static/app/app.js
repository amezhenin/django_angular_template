'use strict';

angular.module('XYZ', [
  'XYZ.login',
  'XYZ.dashboard',
  'XYZ.constants'
])
  .config(function ($stateProvider, $urlRouterProvider, $locationProvider, $logProvider, DEV_SERVER) {
    $urlRouterProvider
      .otherwise('/login');

    $locationProvider.html5Mode(true);

    // turn on $log.debug, when we are in local/dev environment
    $logProvider.debugEnabled(DEV_SERVER);
  });
