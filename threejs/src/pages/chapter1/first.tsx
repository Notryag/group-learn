import { useEffect, useRef } from 'react'
import * as THREE from 'three'



export default function First() {
  const ref = useRef()
  useEffect(() => {
    init()
  }, [])

  const init = () => {
    const scene = new THREE.Scene()
    const geometry = new THREE.BoxGeometry(100, 100, 100)
  
    const material = new THREE.MeshBasicMaterial({
      color: 0xff0000
    })
  
    const mesh = new THREE.Mesh(geometry, material)
    mesh.position.set(0,10,0)
    scene.add(mesh)
  
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000)
    camera.position.z = 8
  
    const render = new THREE.WebGLRenderer()
    render.setSize(window.innerWidth, window.innerHeight)
    render.setClearColor('#af3', .5)
    ref.current!.appendChild(render.domElement)

    render.render(scene, camera)
  }


  return(
    <div>
      <div className="container "  ref={ref}>
      </div>
    </div>
  )
}