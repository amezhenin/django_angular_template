'use strict';

angular.module('XYZ.dashboard', [
  'ui.router',
  'ui.bootstrap'
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('dashboard', {
        url: '/dashboard',
        templateUrl: 'static/app/controllers/dashboard/dashboard.html',
        controller: 'DashboardCtrl'
      });
  })
  .controller('DashboardCtrl', function ($scope) {
    $scope.message = {
      time: new Date(),
      text: "This is dashboard"
    };
  });
