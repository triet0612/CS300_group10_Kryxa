import adapter from '@sveltejs/adapter-static';

export default  {
	kit: {
		adapter: adapter({
			fallback: 'index.html',
			pages: '../www'
		})
	}
};
