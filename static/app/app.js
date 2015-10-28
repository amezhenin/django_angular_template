'use strict';

angular.module('XYZ', [
  'XYZ.login',
  'XYZ.dashboard',
  'XYZ.navbar'
  //'XYZ.constants'
])
  .config(function ($stateProvider, $urlRouterProvider, $locationProvider, $logProvider) {
    $urlRouterProvider
      .otherwise('/login');

    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });


    // turn on $log.debug, when we are in local/dev environment
    //$logProvider.debugEnabled(DEV_SERVER);
  });
