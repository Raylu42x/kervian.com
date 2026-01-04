---
layout: base.njk
title: Projects
bodyClass: glow-purple
---

# Projects

<div class="card-grid">
{% for project in collections.projects | reverse %}
  <div class="card">
    <a href="{{ project.url }}">
      <h2>{{ project.data.title }}</h2>
      <p>{{ project.data.excerpt }}</p>
    </a>
  </div>
{% endfor %}
</div>
