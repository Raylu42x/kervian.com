---
layout: base.njk
title: Portfolio
bodyClass: glow-pink
---

# Portfolio

<div class="card-grid">
{% for item in collections.portfolio %}
  <a href="{{ item.url }}" class="card--portfolio">
    <h2>{{ item.data.title }}</h2>
    <p class="card-excerpt">{{ item.data.excerpt }}</p>

    {% if item.data.portfolioImage %}
      <img src="{{ item.data.portfolioImage }}" alt="{{ item.data.title }}" class="card-image">
    {% else %}
      <div class="card-content">
        {{ item.templateContent | striptags | truncate(500) }}
      </div>
    {% endif %}
  </a>
{% endfor %}
</div>