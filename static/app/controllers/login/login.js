'use strict';

angular.module('XYZ.login', [
  'ui.router',
  'ui.bootstrap'
]).controller('LoginCtrl', function ($scope) {
    $scope.message = {
      time: new Date(),
      text: "This is login"
    };
  });
