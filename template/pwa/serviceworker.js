
const cacheName = 'Online Shopping';
const staticAssets = [
	'/',
	'/static/assets/css/style.css',
]

self.addEventListener('install', async e =>{
	const cache = await caches.open(cacheName);
	await cache.addAll(staticAssets);
	return self.skipWaiting();
});

self.addEventListener('activate', async e =>{
	self.clients.claim();
});

// self.addEventListener('fetch', async e =>{
// 	const req = e.request;
// 	const url = new URL(req.url);

// 	if (url.origin == location.origin) {
// 		e.respondWith(cacheFirst(req));
// 	}
// 	else{
// 		e.respondWith(networkkAndCache(req));
// 	}
// });

self.addEventListener('fetch', function(event) {
const promiseChain = doSomethingAsync()
      .then(() => doSomethingAsyncThatReturnsAURL(event))
      .then(someUrl => fetch(someUrl));
event.respondWith(promiseChain);
});


window.addEventListener('beforeinstallprompt', (e) => {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  e.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = e;
  // Update UI to notify the user they can add to home screen
  addBtn.style.display = 'block';

  addBtn.addEventListener('click', (e) => {
    // hide our user interface that shows our A2HS button
    addBtn.style.display = 'none';
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the A2HS prompt');
        } else {
          console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
      });
  });
});