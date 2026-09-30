const businesses = {
  shiroko: "",
  barber1: "https://share.google/afDHlZuG6RxgHqHrW",
  pizza2: "PUT_GOOGLE_REVIEW_LINK_HERE",
};

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // /shiroko -> shiroko
    const business = url.pathname
      .replace(/^\/+|\/+$/g, "")
      .toLowerCase();

    const reviewUrl = businesses[business];

    if (!reviewUrl) {
      return new Response("Business not found", {
        status: 404,
      });
    }

    return Response.redirect(reviewUrl, 302);
  },
};
