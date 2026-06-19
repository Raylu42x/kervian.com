---
layout: base.njk
title: Home
bodyClass: glow-green
---

<section class="home-hero">
  <img src="https://assets.kervian.com/img/logo.jpeg" alt="Kervian Logo" class="logo-home">
  <h1>Welcome to one of Bennett's Website</h1>
  <p class="home-tagline">Full-stack experiments, games, and things I build for fun.</p>
</section>

<section class="home-section">
  <h2>Featured Projects</h2>
  <div class="card-rail">
  {%- set featuredCount = 0 -%}
  {%- for project in collections.projects -%}
    {%- if project.data.featured -%}{%- set featuredCount = featuredCount + 1 -%}{%- endif -%}
  {%- endfor -%}
  {% for project in collections.projects %}
    {% if featuredCount > 0 and project.data.featured %}
      <div class="card">
        <a href="{{ project.url }}">
          <h2>{{ project.data.title }}</h2>
          <p>{{ project.data.excerpt }}</p>
        </a>
      </div>
    {% elif featuredCount == 0 and loop.index <= 3 %}
      <div class="card">
        <a href="{{ project.url }}">
          <h2>{{ project.data.title }}</h2>
          <p>{{ project.data.excerpt }}</p>
        </a>
      </div>
    {% endif %}
  {% endfor %}
  </div>
  <p class="home-section__link"><a href="/projects/">See all projects →</a></p>
</section>

This is the hub of my empire 
Great!!!
