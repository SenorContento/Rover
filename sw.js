//I am just using this service worker temporarily to debug my PWA (Progressive Web App) until I write a real service worker!
//Hint: Add Cache Busting URLs parameters using rando and ? sort of like utm, but for cache.

'use strict'

const CACHE_NAME = 'cache-v1';
// The files we want to cache
const resourceList = [
  '/offline',
  '/sitedata/manifest.json',
  '/sitedata/opensearch.xml',
  '/sitedata/stylesheets/mobile-stylesheet.css',
  '/sitedata/stylesheets/stylesheet.css',
  '/sitedata/javascripts/printable.js',
  '/sitedata/shadowdom.html',
  '/sitedata/javascripts/loadSW.js',
  '/sitedata/customizations/dropdown.html',
  '/sitedata/images/bkg.png',
  'https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js', //Doesn't seem to work offline. No printable page button!
  '/sitedata/bower_components/polymer/polymer.html',
  '/sitedata/bower_components/polymer/polymer-mini.html',
  '/sitedata/bower_components/polymer/polymer-micro.html',
  '/sitedata/stylesheets/print.css',
  '/sitedata/images/SenorContento-144x144.png',
  '/sitedata/images/SenorContento-1024x1024.png',
  '/sitedata/images/SenorContento-Mask.svg',
  '/sitedata/images/SenorContento.svg'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => {
    return cache.addAll(resourceList);
  }));
});

function addToCache(cacheName, resourceList) {
  caches.open(cacheName).then(cache => {
    return cache.addAll(resourceList);
  });
}

self.addEventListener('fetch', event => {
  /*event.respondWith(
    new Response('This came from the service worker!')
  );*/
  event.respondWith(caches.match(event.request).then(response => {
    return response || fetch(event.request);
  })
    .catch(function() {
      return caches.match('/offline');
    })
  );
});
