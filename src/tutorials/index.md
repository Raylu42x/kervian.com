---
layout: base.njk
title: Tutorials
bodyClass: glow-orange
---

# Tutorials

<div class="card-grid">
{% for tutorial in collections.tutorials | reverse %}
  <div class="card">
    <a href="{{ tutorial.url }}">
      <h2>{{ tutorial.data.title }}</h2>
      <p>{{ tutorial.data.excerpt }}</p>
    </a>
  </div>
{% endfor %}
</div>
