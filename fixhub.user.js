// ==UserScript==
//
// @name fixhub
// @version 0.4
// @namespace lazar6@illinois.edu
// @description https://github.com/davidlazar/fixhub
//
// @match *://github.com/*
//
// @resource fixhubCSS fixhub.css
// @resource iconCSS fixhub-icons.css
// @require http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js
//
// ==/UserScript==

// Add hand-written styles
var fixhubCssText = GM_getResourceText("fixhubCSS");
GM_addStyle(fixhubCssText);

// Add generated icon styles
var iconCssText = GM_getResourceText("iconCSS");
GM_addStyle(iconCssText);

// Replace the user bar icons with text
$('a#new_repo').html('New Repo');
// TODO this hides any settings alerts
$('a#account_settings').html('Settings');
$('a#logout').html('Logout');

// Make the user bar items be minibuttons
$('a#new_repo').addClass('minibutton');
$('a#account_settings').addClass('minibutton');
$('a#logout').addClass('minibutton');

// Hack to fix user bar minibutton hover color
$('#userbox').attr('id', 'fixhub-userbox');

// Remove the repo label ("PUBLIC") on the very left of the page
$('span.repo-label').remove();

// Remove the little clock icon next to "Latest commit to the master branch" 
$('.last-commit span.mini-icon').remove();
