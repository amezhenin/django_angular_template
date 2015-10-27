'use strict';

angular.module('XYZ.navbar', [
  'ui.router',
  'ui.bootstrap'
]).controller('NavbarCtrl', function ($scope) {
    $scope.message = {
      time: new Date(),
      text: "This is Navbar"
    };
  });
