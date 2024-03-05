package main

import (
	"github.com/gin-gonic/gin"
)

var tasks []string

func main() {
	router := gin.Default()

	router.LoadHTMLGlob("templates/*")

	router.GET("/", func(c *gin.Context) {
		c.HTML(200, "index.html", gin.H{
			"tasks": tasks,
		})
	})

	router.POST("/add", func(c *gin.Context) {
		task := c.PostForm("task")
		tasks = append(tasks, task)
		c.Redirect(302, "/")
	})

	router.Run(":8080")
}
