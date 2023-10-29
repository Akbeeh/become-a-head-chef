interface Dictionary<T> {
  [key: string]: T;
}

export interface RecipeInterface {
  day_theme: string;
  date: string;
  url: string;
  info_recipe: RecipeDetailsInterface;
}

export interface RecipeDetailsInterface {
  title: string;
  description: string;
  about_recipe: Dictionary<string>;
  nutrition: Dictionary<string>;
}
