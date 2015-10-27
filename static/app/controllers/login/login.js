'use strict';

angular.module('XYZ.login', [
  'ui.router',
  'ui.bootstrap'
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('login', {
        url: '/login',
        templateUrl: 'app/controllers/login/login.html',
        controller: 'LoginCtrl'
      });
  })
  .controller('LoginCtrl', function ($scope) {
    $scope.message = {
      time: new Date(),
      text: "This is login"
    };
  });
